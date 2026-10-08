import os
import easyocr
import pandas as pd
from tqdm import tqdm  # İlerleme çubuğu görmek için

def gorselleri_csvye_aktar(ana_klasor="veriseti_hazirlama", cikis_csv="veri_seti.csv"):
    # EasyOCR okuyucusunu başlat (Türkçe ve İngilizce)
    print("🤖 EasyOCR modeli yükleniyor...")
    reader = easyocr.Reader(['tr', 'en'], gpu=False) # GPU varsa True yapabilirsin
    
    veri_listesi = []
    alt_klasorler = ['0', '1'] # 0 = Güvenli, 1 = Dolandırıcı
    
    for etiket in alt_klasorler:
        klasor_yolu = os.path.join(ana_klasor, etiket)
        
        if not os.path.exists(klasor_yolu):
            print(f"⚠️ Klasör bulunamadı: {klasor_yolu}, atlanıyor...")
            continue
            
        print(f"📂 '{etiket}' klasöründeki görseller işleniyor...")
        gorseller = [f for f in os.listdir(klasor_yolu) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        # tqdm ile terminalde % kaçının bittiğini görebilirsin
        for gorsel_adi in tqdm(gorseller):
            gorsel_tam_yolu = os.path.join(klasor_yolu, gorsel_adi)
            
            try:
                # Görseldeki metinleri oku
                sonuclar = reader.readtext(gorsel_tam_yolu)
                # Tüm tespit edilen satırları aralarında boşluk bırakarak birleştir
                gorsel_metni = " ".join([sonuc[1] for sonuc in sonuclar])
                
                # Eğer görsel bomboşsa veya metin bulunamadıysa boş kalmasın
                if not gorsel_metni.strip():
                    gorsel_metni = "[METIN_BULUNAMADI]"
                
                # Listeye ekle
                veri_listesi.append({
                    "metin": gorsel_metni,
                    "etiket": int(etiket)
                })
            except Exception as e:
                print(f"❌ {gorsel_adi} işlenirken hata oluştu: {str(e)}")
                
    # Pandas DataFrame oluştur ve CSV olarak kaydet
    df = pd.DataFrame(veri_listesi)
    df.to_csv(cikis_csv, index=False, encoding='utf-8-sig')
    print(f"✅ İşlem tamamlandı! Toplam {len(df)} satır veri '{cikis_csv}' dosyasına kaydedildi.")

# Kodu çalıştır
if __name__ == "__main__":
    gorselleri_csvye_aktar()
