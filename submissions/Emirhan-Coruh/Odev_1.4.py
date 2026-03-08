# 2.görev
# Yazdığımız matematik_yardimcisi modülünü import ile içe aktarıyoruz.
import matematik_yardimcisi

sayilar = (13,35,73,956,25,9,346,46) # Dümenden bir tuple(demet) oluşturuyoruz.
# demet(tuple) içindeki verileri * (unpacking) operatörü ile ayıklıyoruz 
# yoksa iki üst üste biniyor ve hata veriyor.
ort = matematik_yardimcisi.ortalama(*sayilar)
print(ort)

# --------------------------------------------------------------------------------------------
# 3. Görev

# Bir kelime listesi belirledim.
kelimeler = ["Ev", "Gitar", "Kod", "Veri", "Kamera"]

# sorted fonksiyonuna "key" olarak bir lambda fonksiyonu veriyoruz.
# Bu sayede koşulumuzu belirliyoruz ve kelimeler buna göre sıralanıyor.
sirali_kelimeler = sorted(kelimeler, key = lambda x: len(x))
print(sirali_kelimeler)

# --------------------------------------------------------------------------------------------
# 4. Görev

# ad, fiyat, stok_adedi zorunlu parametrelerimiz, **kwargs ise ekstra özellik almamızı sağlar
def urun(ad, fiyat, stok_adedi, **kwargs):
    print("------------------------")
    print("--- Ürün Özellikleri ---")
    print(f"> Ürün Adı: {ad}")
    print(f"> Ürün Fiyatı: {fiyat}")
    print(f"> Stok Adedi: {stok_adedi}")

    # Eğer fonksiyona ekstra özellik(kwargs) girilirse bu bloğa yönlendiriliyor.
    if kwargs:
        print("-- Ekstra Özellikler --")
        # kwargs bir sözlük(dictionary) olduğu için .items() ile key-value ikililerini alıyoruz.  
        for key, value in kwargs.items():
            # Çıktıların estetik gözükmesi için .replace() ve .title() kullandım bu kısım zorunlu değil.
            # basit bir şekilde "{key}: {value}" olarak da yazılabilir.
            print(f"> {key.replace('_',' ').replace('u','ü').title()}: {value}")
    
    print("-------------------------\n") # Bir arayüzmüş gibi gözükmesi için.

# Fonksiyonun kullanım şekli:
urun("Kamera", "€750", 20, uretim_yeri = "Almanya", garanti_suresi = "2 Yıl")
