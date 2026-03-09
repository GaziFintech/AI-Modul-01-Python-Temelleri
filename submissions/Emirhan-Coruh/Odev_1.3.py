# 1. görev
import random

# Bilgisayara 1 ile 20 arasında sayı tutturuyoruz.
pc_sayi = random.randint(1, 20)
tahmin = 0

# Kullanıcı doğru sayıyı bulana kadar çalışacak bir döngü başlatıyoruz.
while tahmin != pc_sayi:
    tahmin = int(input("Sayıyı tahmin ediniz: "))
    
    # Tahmin edilen sayının belirlenen aralıkta olup olmadığını kontrol ediyoruz.
    if tahmin < 1 or tahmin > 20:
        print("Geçersiz sayı girdiniz!")

    # Sayının tamini için kullanıcıya gerekli yönlendirmeleri yapıyoruz.
    elif tahmin < pc_sayi:
        print("Yukarı")
    elif tahmin > pc_sayi:
        print("Aşağı")
    # Doğru tahmin yapıldığında break komutu ile döngüyü bitiriyoruz.
    else:
        print("Doğru tahmin!")
        break

# 2. Görev
# 1'den 50'ye kadar tüm sayıları for döngüsü ile sırayla işleme alıyoruz.
for i in range(1, 51):
    # Sayıların modunu alarak 3'e bölünüp bölünmediğini kontrol ediyoruz.
    if i % 3 == 0:
        print(i, end = " ") # Sayıları tek satırda göstermek istedim bu yüzden (end) kullandım.


# 3. Görev
print()
sayi_liste = [13,15,28,69,16,22,682,77,27,59,35,80,2,5,9,63,8,76,14] # Bu listeyi kafama göre oluşturdum.

# Mevcut listedeki sayıları sırayla işleme alıyoruz ve 
# tek bir satırda(List Comprehension) bütün döngüyü kurarak
# yeni bir listeye atıyoruz.
yeni_liste = [j**2 for j in sayi_liste if j % 2 == 0]
print(f"Çift sayıların karesinin bulunduğu yeni listemiz: {yeni_liste}")