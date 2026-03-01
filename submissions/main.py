import string
from operator import truediv

ad = input("Ad giriniz: ")
soyad = input("Soyad giriniz: ")
yas = int(input("Yas giriniz: "))
sicaklik = float(input("Sicaklik giriniz: "))

f = sicaklik * 1.8 + 32

resit_mi = 0

if yas > 18:
    resit_mi = 1

print("Merhaba " + ad + " " + soyad + "," + str(yas) + " yasindasiniz. Resitlik durumu: " + str(bool(resit_mi)))
print("Girdiginiz " + str(sicaklik) + " derece, " + str(f) + " fahrenheita esittir.")

