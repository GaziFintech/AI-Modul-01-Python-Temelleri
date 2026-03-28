ogrenci_notlari = {}

okul = "gazi", 1926

for x in range(3):
    name = input("Öğrenci Adı: ")
    grade1 = input("Öğrenci Notu 1: ")
    grade2 = input("Öğrenci Notu 2: ")
    grade3 = input("Öğrenci Notu 3: ")
    ogrenci_notlari[name] = {"Not 1": grade1, "Not 2": grade2, "Not 3": grade3}

print(ogrenci_notlari)

ogrenci_adlari = set(ogrenci_notlari.keys())
print(ogrenci_adlari)

print(f"Toplam Öğrenci Sayısı: {len(ogrenci_adlari)}")

ogr = input("Hangi öğrenciye erişmek istiyorsunuz: ")
ogr_not = input("Hangi nota erişmek istiyorsunuz (Not 1, Not 2, Not 3): ")

print(f"Öğrenci Adı: {ogr}, İstenen Öğrenci Notu: {ogrenci_notlari[ogr][ogr_not]}")
