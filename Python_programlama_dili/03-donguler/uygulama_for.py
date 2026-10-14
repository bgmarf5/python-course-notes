sayilar = [3,5,8,99,12,34]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız.
#for i in sayilar:
 #   print(i)
# 2- "sayilar" listesindeki hangi sayılar 2' nin katı
#for i in sayilar:
#   if (i % 2 == 0):
#      print(i)
# 3- "sayilar" listesinde tüm sayıların toplamı 
toplam = 0
for i in sayilar:
    toplam += i
    print(toplam)
  # Not: print(toplam) ı for döngüsü içerisine yazılırsa toplaya toplaya gider. Eğer for un dışına yazılırsa sadece toplamı yazar. 

urunler = ["samsung s24", "samsung s22", "iphone 15", "iphone 14"]

# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (find , index)
for i in urunler:
    if( i.find("samsung")):
        print(i)


for i in urunler:
    index = i.find('iphone')
    if index > -1:
        print(i)


# 5- "urunler" listesinde kaç adet samsung ürünü vardır
adet = 0
for i in urunler:
    index = i.find('samsung')
    if index > -1:
        adet += 1

print(adet)

#dictinory(sozlük) veri tipleri hakkında örnekleri

ogrenciler = [
    {"ogrenciNo":1234 , "ogrenciAdi":"Ayşe"},
    {"ogrenciNo":123 , "ogrenciAdi":"Fatma"},
    {"ogrenciNo":12345 , "ogrenciAdi":"Hayriye"}
]

# 1- Aşağıdaki örnek cümleyi tum ogrencilere uygulayınız
# "123 numaralı öğrencinin ismi Ayşedir"

for ogr in ogrenciler:
    print(f'{ogr["ogrenciNo"]} numaralı öğrenxinin ismi {ogr["ogrenciAdi"]}')


# 2- oğrencilerin numaraları toplamı
toplam = 0
for ogr in ogrenciler:
    toplam += ogr["ogrenciNo"]
print(toplam)


# 3- 123 ile 12345  arasıdaki öğrencileri listeleyiniz
# 3.1
for sira in ogrenciler:
    sayi = sira["ogrenciNo"]
    if (sayi > 123 and sayi < 12345) :
        print(f"{sira['ogrenciAdi']}")
        

# 3.2
for sira in ogrenciler:
    if(sira["ogrenciNo"] >= 123 and sira["ogrenciNo"] <= 12345):
        print(f'{sira["ogrenciAdi"]}')


# 4- kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz
no = int(input(" Lütfen öğrenci numarasını giriniz: "))
for sira in ogrenciler:
    sayi = sira["ogrenciNo"]
    if (sayi == no):
        print(f'girdiğiniz {no} numarasına ait öğrencinin adı {sira["ogrenciAdi"]}')

# öğrenci adına göre arama

isim = input(" lütfen öğrenci ismini giriniz : ")

for isimler in ogrenciler:
    if(isimler["ogrenciAdi"].lower().find(isim.lower()) > -1):
        print(f'{isimler["ogrenciAdi"]}')