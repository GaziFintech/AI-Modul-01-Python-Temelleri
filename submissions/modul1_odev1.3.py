import random

number = random.randrange(1,20)

tahmin = int(input("Bir sayı tahmin ediniz: "))

while tahmin != number:

    if tahmin < number:
        tahmin = int(input("Bilemediniz daha büyük bir sayı tahmin ediniz: "))
    elif tahmin > number:
        tahmin = int(input("Bilemediniz daha küçük bir sayı tahmin ediniz: "))
    if tahmin == number:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break

print("-------------------------------------------")

for i in range(1, 50):
    if i % 3 == 0:
        print(i, end=" ")

print("\n-------------------------------------------")

sayilar = [2, 3, 4, 8, 9, 11, 14, 16, 17]

for i in sayilar:
    if i % 2 == 0:
        print(i*i, end=" ")
