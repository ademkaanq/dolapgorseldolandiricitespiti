import os
import re
import easyocr
import joblib

def metin_temizle(metin):
    metin = str(metin).lower()
    metin = metin.replace('o', '0')
    metin = re.sub(r'[^\w\s\d]', ' ', metin)
    return metin

def canli_ilan_test_et(gorsel_yolu):
        
    reader = easyocr.Reader(['tr', 'en'], gpu=False) 
    
    sonuclar = reader.readtext(gorsel_yolu)
    ocr_metni = " ".join([sonuc[1] for sonuc in sonuclar])
        
    print(f"\nOCR Çıktısı: {ocr_metni}")

    temiz_ocr_metni = metin_metni = metin_temizle(ocr_metni)
        
    model = joblib.load("dolandirici_modeli.pkl")
    vektorlestirici = joblib.load("vektorlestirici.pkl")

    vektorize_metin = vektorlestirici.transform([temiz_ocr_metni])
    tahmin = model.predict(vektorize_metin)[0]
    olasiliklar = model.predict_proba(vektorize_metin)[0]
        
    print("\n--- Analiz sonucu")
    if tahmin == 1:
        print(f"Bu görsel muhtemelen dolandırıcıya ait")
        print(f"Dolandırıcılık Olasılığı: %{olasiliklar[1]*100:.1f}")
    else:
        print(f"Güvenli")
        print(f"Temiz Olma Olasılığı: %{olasiliklar[0]*100:.1f}")

if __name__ == "__main__":
    test_gorseli = "test_resmi.png" 
    canli_ilan_test_et(test_gorseli)
