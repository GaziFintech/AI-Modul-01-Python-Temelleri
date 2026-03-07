# Değişkenlerin tanımlanması.
ad = input("Adınızı giriniz: ")
soyad = input("Soyadınızı giriniz: ")
yas = int(input("Yaşınızı giriniz: "))
sicaklik = float(input("Celsius cinsinden sıcaklık değerini giriniz: "))

# Celsius sıcaklığın Fahrenheit birimine dönüştürülmesi.
fahrenheit = (sicaklik * 1.8) + 32

# Mantıksal kontrol ile kullanıcının reşit olup olmadığı kontrol edilir.
resit_mi = yas >= 18

# Çıktının string formatlama yöntemi ile yazdırılması.
print(f"Merhaba {ad} {soyad}, {yas} yaşındasınız. Reşitlik durumu: {resit_mi}. Girdiğiniz {sicaklik:.2f} Celsius derece, {fahrenheit:.2f} Fahrenheit'a eşittir.")