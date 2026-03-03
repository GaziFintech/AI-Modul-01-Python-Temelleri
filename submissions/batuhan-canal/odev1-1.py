ad = input("Adınızı giriniz: ")
soyad = input("Soyadınızı giriniz: ")
yas = int(input("Yaşınızı giriniz: "))
sicaklik = float(input("Celsius cinsinden sıcaklık değerini giriniz: "))

fahrenheit = (sicaklik * 1.8) + 32

resit_mi = yas >= 18

print(f"Merhaba {ad} {soyad}, {yas} yaşındasınız. Reşitlik durumu: {resit_mi}. Girdiğiniz {sicaklik:.2f} Celsius derece, {fahrenheit:.2f} Fahrenheit'a eşittir.")