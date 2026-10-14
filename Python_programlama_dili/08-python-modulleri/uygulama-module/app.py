"""
    module1(db)     : urunler
    module2(methods): urunEkle(), urunGüncelle(), urunGetir()
    module3(app)    :

        yeni ürün ekleme => urunEkle("iphone 15", 60000)
        ürün güncelle    => urunGuncelle(1, "iphone 15 pro", 80000)
        ürünleri listele => urunleriGetir()
"""


from methods import *

urunEkle("iphone 20", 100000)
urunEkle("samsung s20", 100000)
urunGuncelle(2,"iphone 15 prog", 75000)

 
for i in urunleriGetir():
    print(i["urunAdi"])