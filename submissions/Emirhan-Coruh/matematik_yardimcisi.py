# Odev_1.4 / 1. Görev
# Ortalamayı döndürecek fonksiyonu yazıyoruz.
def ortalama(*args):
    # Sıfıra bölünmesi sonucu hata almamak için bir ön kontrol yapıyoruz.
    if len(args) == 0:
        return 0

    toplam = 0
    # Girilen tüm sayıları sırayla dönerek toplam'a ekliyoruz.
    for sayi in args:
        toplam += sayi
    # toplam'ı bulunan sayı adedine bölerek ortalamayı döndürüyoruz.
    return toplam/len(args)

