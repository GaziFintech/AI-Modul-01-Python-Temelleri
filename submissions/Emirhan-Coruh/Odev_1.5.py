# Hesap adında bir sınıf(class) oluşturuyoruz.
class Hesap:
    def __init__(self):
        # "__bakiye" değişkenini gizli hale getiriyoruz böylece dışardan erişime kapanıyor.
        self.__bakiye = 50

    def para_yatir(self, yatirilan_para):
        # Bakiye değişkenine para eklemek için para_yatir metodunu oluşturuyoruz.
        self.__bakiye += yatirilan_para
        print(f"Hesabınıza {yatirilan_para} TL para girişi oldu.")

    def para_cek(self, cekilen_para):
        # Bakiye kontrolü yapmak için if/else bloğu kuruyoruz çünkü mevcut 
        # bakiyeden daha fazla miktarda para çekilemez.
        if cekilen_para <= self.__bakiye:
            self.__bakiye -= cekilen_para
            print(f"Hesabınızdan {cekilen_para} TL para çekildi, yeni bakiye: {self.__bakiye} TL")
        else:
            print(f"Yetersiz Bakiye!")

    def bakiye_sorgula(self):
        # Bakiyeyi sorgulamak için bakiye_sorgula metodunu oluşturuyoruz.
        return self.__bakiye

# Hesap sınıfının özelliklerini kullanan bir Vadeli Hesap sınıfı oluşturuyoruz.
class VadeliHesap(Hesap):
    def para_cek(self, cekilen_para):
        # Çekilen para üzerinden %5 oranında işlem ücreti hesaplanıyor.
        islem_ucreti = cekilen_para*(0.05)
        toplam_cekilen = cekilen_para + islem_ucreti
        
        # Ana sınıfa dışardan erişim olmadığı için super() fonksiyonu kullanıyoruz.
        super().para_cek(toplam_cekilen)

# Kullanım:
print("------------------ Normal Hesap --------------------")
Hesabim = Hesap()
Hesabim.para_yatir(1000)
Hesabim.para_cek(30)
print(f"Mevcut Bakiye: {Hesabim.bakiye_sorgula()} TL")
print("----------------------------------------------------")

print("------------------ Vadeli Hesap --------------------")
Vadeli_Hesabim = VadeliHesap()
Vadeli_Hesabim.para_yatir(1000)
Vadeli_Hesabim.para_cek(100)
print(f"Mevcut Bakiye: {Vadeli_Hesabim.bakiye_sorgula()} TL")
print("----------------------------------------------------")

