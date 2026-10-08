import os
import re
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

def metin_temizle(metin):
    metin = str(metin).lower()
    metin = metin.replace('o', '0')  # Dolandırıcıların meşhur 'o' hilesi
    metin = re.sub(r'[^\w\s\d]', ' ', metin)  # Noktalamaları kaldır, sayıları koru
    return metin

def modeli_egit(csv_yolu="veri_seti.csv"):
    if not os.path.exists(csv_yolu):
        raise FileNotFoundError(f"❌ '{csv_yolu}' dosyası bulunamadı! Lütfen veri setini hazırlayın.")
        
    print(f"📂 Veriler '{csv_yolu}' dosyasından yükleniyor...")
    df = pd.read_csv(csv_yolu, encoding='utf-8-sig')
    
    print("🧹 Metin ön işleme adımı yapılıyor...")
    df['temiz_metin'] = df['metin'].apply(metin_temizle)
    
    print("🧠 TF-IDF dönüşümü ve Lojistik Regresyon eğitimi başlatıldı...")
    # Sınıflandırıcı ve Vektörleştirici tanımlanıyor
    vektorlestirici = TfidfVectorizer(ngram_range=(1, 2))
    X_train_vektor = vektorlestirici.fit_transform(df['temiz_metin'])
    y_train = df['etiket']
    
    model = LogisticRegression()
    model.fit(X_train_vektor, y_train)
    
    # Modelin kendi üzerindeki performansını görelim
    tahminler = model.predict(X_train_vektor)
    print(f"🎯 Eğitim Doğruluk Oranı: {accuracy_score(y_train, tahminler):.2%}")
    
    print("💾 Modeller bilgisayara kaydediliyor...")
    joblib.dump(model, "dolandirici_modeli.pkl")
    joblib.dump(vektorlestirici, "vektorlestirici.pkl")
    print("✅ 'dolandirici_modeli.pkl' ve 'vektorlestirici.pkl' başarıyla oluşturuldu!")

if __name__ == "__main__":
    modeli_egit()
