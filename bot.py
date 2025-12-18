import requests
import time

# 1. AYARLAR: Burayı kendine göre değiştir
HEDEF_URL = "https://avukatbeta.uyap.gov.tr" # Buraya kontrol etmek istediğin siteyi yaz
KONTROL_ARALIGI = 15 # Kaç saniyede bir kontrol edilsin?

# Tarayıcı gibi görünmek için başlık bilgisi
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def siteyi_tara():
    print(f"--- {HEDEF_URL} kontrol ediliyor... ---")
    try:
        # Siteye istek atıyoruz
        cevap = requests.get(HEDEF_URL, headers=HEADERS, timeout=10,allow_redirects=True)
        
        if cevap.status_code == 200:
            print(f"✅ Durum: AKTİF (Kod: 200)")
        elif cevap.status_code == 404:
            print(f"❓ Durum: SAYFA BULUNAMADI (Kod: 404).")
        else:
            print(f"⚠️ Durum: SORUNLU (Kod: {cevap.status_code})")
            
    except requests.exceptions.ConnectionError:
        print("❌ HATA: Siteye ulaşılamıyor!")
    except Exception as e:
        print(f"❌ BEKLENMEYEN HATA: {e}")


if __name__ == "__main__":
    while True:
        siteyi_tara()
        print(f"{KONTROL_ARALIGI} saniye sonra tekrar kontrol edilecek...\n")
        time.sleep(KONTROL_ARALIGI)