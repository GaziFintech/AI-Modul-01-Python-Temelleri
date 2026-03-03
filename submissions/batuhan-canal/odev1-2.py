ogrenci_notlari = {"Batuhan" : [79, 87, 67], "Ahmet" : [67, 45, 92], "Veli" : [90, 23, 56], "Mustafa": [42, 49, 87]}
ogrenci_isimleri = set(ogrenci_notlari.keys())
okul_detaylari = ("Gazi Üniversitesi", 1926)

print(f"Batuhan adlı öğrencinin ikinci notu: {ogrenci_notlari['Batuhan'][1]} ve toplam öğrenci sayısı ise {len(ogrenci_notlari.keys())}")

