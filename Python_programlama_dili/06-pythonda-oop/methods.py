 # Class
class Product:
    
    #attribute, property,ozellik
    def __init__(self, name, price, isActive):#yapıcı methot atribute property eklemek için nesne çaprildığında çalışır çağrilir
        self.name = name
        self.price =price
        self.isActive = isActive

    # -instance-method  =sınıfa özel  görev yapan işlevsellik kazandıran fonksiyonlar olarak tanımlanır
    def get_product(self):
        return f"urun adi: {self.name} urun fiyatı: {self.kdv_price()}"
    
    def kdv_price(self):
        return self.price * 1.20




# Instance, Nesne, Obje
p1 = Product("Iphone 15",50000, True)# sınıfından p1 nesnesi
p2 = Product("Iphone 15 Pro",60000, False)# nesnelerimizin özellikleri yapıcı methodumuzdan alırız dışıarıdan verliken parametlerir nesnenin ozelliklerine eşıtleriz
p3 = Product("Samsung S24",70000,True)

# sonuc = p1.name
# sonuc = p2.price
# sonuc = p3.isActive
# print(sonuc)
urunler = [p1, p2, p3]
for urun in urunler:
    if urun.isActive:
        print(urun.get_product())
        print(urun.kdv_price())