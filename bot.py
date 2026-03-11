import requests
import tweepy
import time
import urllib3
import os
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

HEDEF_URL = "https://avukatbeta.uyap.gov.tr/"
KONTROL_ARALIGI = 60       # Kaç saniyede bir kontrol (1 dakika)
TWEET_BEKLEME_SURESI = 1800 # Aynı hata için kaç saniyede bir tweet (30 dakika)


API_KEY             = os.getenv("API_KEY")
API_SECRET          = os.getenv("API_SECRET")
ACCESS_TOKEN        = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# Durum takibi
son_tweet_zamani = 0
site_onceki_durumu = True  

def tweet_at(mesaj):
    try:
        client = tweepy.Client(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )
        client.create_tweet(text=mesaj)
        print("✅ Tweet atıldı!")
    except Exception as e:
        print(f"❌ Tweet atılamadı: {e}")

def zaman():
    return datetime.now().strftime("%H:%M:%S")

def siteyi_tara():
    global son_tweet_zamani, site_onceki_durumu
    simdi = time.time()
    tweet_gonderlebilir = (simdi - son_tweet_zamani) >= TWEET_BEKLEME_SURESI

    try:
        cevap = requests.get(HEDEF_URL, headers=HEADERS, timeout=10, allow_redirects=True)

        if cevap.status_code == 200:
            print(f"[{zaman()}] ✅ AKTİF (Kod: 200)")

            # Site tekrar açıldıysa bildir
            if not site_onceki_durumu:
                mesaj = f"✅ ÇÖZÜLDÜ: {HEDEF_URL} tekrar erişilebilir durumda! #UYAP #SistemAktif"
                tweet_at(mesaj)
                son_tweet_zamani = simdi

            site_onceki_durumu = True

        elif cevap.status_code == 404:
            print(f"[{zaman()}] ❓ SAYFA BULUNAMADI (Kod: 404)")
            site_onceki_durumu = False
            if tweet_gonderlebilir:
                mesaj = f"❓ UYARI: {HEDEF_URL} bulunamıyor! (Kod: 404) #UYAP #SistemDown"
                tweet_at(mesaj)
                son_tweet_zamani = simdi

        else:
            print(f"[{zaman()}] ⚠️ SORUNLU (Kod: {cevap.status_code})")
            site_onceki_durumu = False
            if tweet_gonderlebilir:
                mesaj = f"⚠️ UYARI: {HEDEF_URL} sorunlu! Durum Kodu: {cevap.status_code} #UYAP #SistemDown"
                tweet_at(mesaj)
                son_tweet_zamani = simdi

    except requests.exceptions.Timeout:
        print(f"[{zaman()}] ⏱️ ZAMAN AŞIMI")
        site_onceki_durumu = False
        if tweet_gonderlebilir:
            mesaj = f"⏱️ UYARI: {HEDEF_URL} zaman aşımına uğradı! #UYAP #SistemDown"
            tweet_at(mesaj)
            son_tweet_zamani = simdi

    except requests.exceptions.ConnectionError:
        print(f"[{zaman()}] ❌ BAĞLANTI HATASI")
        site_onceki_durumu = False
        if tweet_gonderlebilir:
            mesaj = f"❌ ACİL: {HEDEF_URL} çökmüş olabilir! Bağlantı kurulamıyor. #UYAP #Çöktü"
            tweet_at(mesaj)
            son_tweet_zamani = simdi

    except Exception as e:
        print(f"[{zaman()}] ❌ BEKLENMEYEN HATA: {e}")

if __name__ == "__main__":
    print(f"🚀 Bot başlatıldı. Her {KONTROL_ARALIGI // 60} dakikada bir kontrol edilecek.")
    while True:
        siteyi_tara()
        print(f"⏳ {KONTROL_ARALIGI} saniye bekleniyor...\n")
        time.sleep(KONTROL_ARALIGI)