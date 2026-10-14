"""
** BankaHesabi isminde bir sınıf tanımlayınız.
** Üretilen her bir nesne "hesaSahibi" isminde bir özelliğe sahip olmalıdır. BankaHesabi("Sadıka Turan")
** Üretilen her vir nesne "baskiye" isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
** Üretilen her bir nesne için "paraYatir" metodu oluşturun ve dışarıdan yatıralacak miktar bilgisini alıp bakiye üzerine ekleyin ve bakiye miktarını geriye döndürün.
** Üretilen her bir nesne için" paraCek" metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp bakiye değerinden çıkarıp geriye döndürün.


        hesap = BankaHesabi("Elif Doğan")
        hesap.hesapSahibi => Elif Doğan 
        hesap.bakiye => 0.0
        hesap.paraYatir(1000)  => 1000.0
        hesap.paraCek(500)  => 500.0
"""
class BankaHesabi:
    def __init__(self, hesapSahibi):
        self.hesapSahibi = hesapSahibi
        self.bakiye = 0

    def get_hesapSahibi(self):
        return f"Hesap Sahibi : {self.hesapSahibi}  Hesap Bakiyesi: {self.bakiye}"

    def paraYatir(self,Ymiktar):
        self.bakiye += Ymiktar
        return self.bakiye
       
    def paraCek(self,Cmiktar):
        self.bakiye -= Cmiktar
        return self.bakiye
    

h1 = BankaHesabi("Elif Doğan")
h1.paraYatir(1234)
h1.paraCek(234)
print(h1.get_hesapSahibi())