import requests
import tweepy
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

# --- AYARLAR ---
HEDEF_URL = "https://avukatbeta.uyap.gov.tr/"
KONTROL_ARALIGI = 300 

# Twitter API 
API_KEY = "yqWIV3O77GAt5W30E1KiUBEvV"
API_SECRET = "lQFpJztzTw2kgykY5x6LFbg5MyO3wZMyhAj0CQ5HmpOoe3CxeB"
ACCESS_TOKEN = "2001654927182180353-OeZ8GsupD4AlHBlmKIelR4S9w2Zk9b"
ACCESS_SECRET = "HNXElQo81JbMT3wh04goQtxAmkWssexh0ceNc5HA30lgz"

# Twitter Bağlantısı
def tweet_at(mesaj):
    try:
        # X API v2 Kullanımı
        client = tweepy.Client(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_SECRET
        )
        client.create_tweet(text=mesaj)
        print("✅ Tweet başarıyla atıldı!")
    except Exception as e:
        print(f"❌ Tweet atılamadı: {e}")

def siteyi_tara():
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        cevap = requests.get(HEDEF_URL, headers=headers, timeout=15)
        
        if cevap.status_code != 200:
            mesaj = f"⚠️ UYARI: {HEDEF_URL} adresine ulaşılamıyor! Durum Kodu: {cevap.status_code} #UYAP #SistemDown"
            print(mesaj)
            tweet_at(mesaj)
        else:
            print(f"✅ {HEDEF_URL} sorunsuz çalışıyor.")

    except Exception:
        mesaj = f"❌ ACİL: {HEDEF_URL} çökmüş olabilir! Bağlantı kurulamıyor. #UYAP #Çöktü"
        print(mesaj)
        tweet_at(mesaj)

if __name__ == "__main__":
    while True:
        siteyi_tara()
        time.sleep(KONTROL_ARALIGI)