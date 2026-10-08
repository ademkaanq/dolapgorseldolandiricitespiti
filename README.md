# dolapgorseldolandiricitespiti
bu proje dolapta görselden platform dışı bir yere gönderen görselleri tespit edilmesini sağlar basit bir ikili sınıflandırma modeli ile easy ocr i birleştirdim 3 tane görselde test ettim ve doğru sonuç verdi.

öncelikle görsel easyocr ile analiz edilir sonra görsel filtrelenir mesela dolandırıcılar 0 ı o olarak yazar bizde o ları 0 a çeviririz. en son ikili sınıflandırma modelimize gönderilir temiz text.

bazı dolandırıcılar dolap sistemlerinin açıklamaya telefon numarası koyunca tespit edildiklerini anladı ve artık 2. görsele telefon numaralarını bırakıyorlar ve onu aramalarını söylüyorlar böylece dolap uygulamasındaki güvenli ödeme sisteminin dışına çıkabilsinler.

dolap sistemlerine daha gelişmiş bir versiyonunun entegre edilebileceğini düşünüyorum ben tek kişiydim çok az veri hazırladım gelişmiş bir model yapmadım ama dolap sistemlerine hem görseli hem açıklamayı hem başlığı hemde kullanıcının diğer ürünlerini inceleyecek multi modal bir model yapılabilir ve böylece dolandırıcılara karşı çok güvenli bir sistem kurabilirler bence.

evet şimdi 3 test sonucunu size göstereyim;


1. test çıktısı : --- Analiz sonucu
Güvenli
Temiz Olma Olasılığı: %55.2
<img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/e025bf77-ffdd-4744-a17a-ff2e145f024f" />

....



2.test çıktısı : --- Analiz sonucu
Bu görsel muhtemelen dolandırıcıya ait
Dolandırıcılık Olasılığı: %64.4
<img width="1080" height="2235" alt="image" src="https://github.com/user-attachments/assets/555dc787-2f4a-4c66-b912-e6f69972b6cc" />



...


3.test çıktısı: --- Analiz sonucu
Bu görsel muhtemelen dolandırıcıya ait
Dolandırıcılık Olasılığı: %62.1

<img width="1080" height="2147" alt="image" src="https://github.com/user-attachments/assets/e63d0673-b215-4c5c-8a1a-0ec004bca7fe" />
