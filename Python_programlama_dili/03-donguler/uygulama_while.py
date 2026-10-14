# 1- Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız
start = int(input("Başlangıç değerini giriniz: "))
stop = int(input("Bitiş değerini giriniz: "))
while (start < stop):
    if (start % 2 == 0):
        print(start)
    start += 1
    
# 2- (1-100) arasındaki sayıları azalan şeklinde yazdırınız,
# i = 100
# while i > 1:
#     print(i)
#     i -= 1

# 3- kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
# t = 1
# while t < 6:
#     sayi = int(input("Lütfen bir sayı giriniz: "))
#     t += 1
#     print(sayi)

# 3.2
# i = 0
# sayilar = []
# while ( i < 5):
#     sayi = int(input("sayı: "))
#     sayilar.append(sayi) #listenin sonuna sayi ekler
#     i += 1

# sayilar.sort()

# print(sayilar)


# 4- klavyeden girişi istenen username bilgisi için boşluk girildiği sürece tekrar username girişi isteyiniz.
isim =""
while not isim:
    isim = input("Kullanıcı adı bilgisini giriniz: ")
print(isim)









#  5-  Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
#    ** dictionary listesi yapısı (ogrenciNo, ogrenciAdi, ogrenciSoyadi) şeklinde olsun.
#    ** ögrenci ekleme işlemi bittiğinde öğrencileri listeleyiniz

ogrenciler =[]
  
n = int(input("Kaç öğrnci gireceksiniz: "))

i = 0
 
while i < n:
    print(f"\n{i + 1}. öğrenci bilgilerini giriniz: ")# {i + 1} öğrencinin kaçıncı olduğunu göstermek
    no = input("Öğrenci No: ")
    ad = input("Öğrenci Adi:")
    soyad = input("Öğernci Soyadı: ")


    ogrenci = { 
        "ogrenciNo":no,
        "ogrenciAdi":ad,
        "ogrenciSoyad":soyad
    }

    ogrenciler.append(ogrenci)

    i += 1


print("-------------Ogrenci Listesi---------")

for org in ogrenciler:
    print(f'{org["ogrenciNo"]}-{org["ogrenciAdi"]}  {org["ogrenciSoyad"]}')




