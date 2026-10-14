"""kursAdi = "  Python ile Programlama"
kursAciklama = " Güzel bir kurs"
kurssaati = "20 saat"

mesaj = "kursun adı: " + kursAdi + "kurs açıklaması : " + kursAciklama + "kursun süresi : " +kurssaati 

print(mesaj[5])
"""
"""
title = "Python ile Programlama Dersleri"
# 1- 'title' değişkeni içerisindeki karakter sayısı nedir?
#print(len(title))

# 2- 'title' içerisindeki 'python' kelimesini alın
#print(title[:6])


# 3- 'title' değişkeninin ilk 5 ve son 5  karakterin alın
#print(title[:6])
#print(title[-8:])

# 4- 'title' değişkenini tersten yazdırınız
#print(title[::-1])

# 5- klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırınız
#     örnek: Çınar Turan isimli öğreninin 1.notu 60, 2. notu 60 ve not ortalamadı 60 olarak hesaplanmıştır


ad=input("öğrenci adı giriniz :")
soyad= input("öğrenci soyad giriniz :")
not_1=int(input("1.notu girin :"))
not_2=int(input("2.notu girin :"))

not_ort= (not_1 + not_2) / 2 

print(f"{ad} {soyad} isimli öğreninin 1.notu {not_1}, 2. notu {not_2} ve not ortalamadı {not_ort} olarak hesaplanmıştır")
"""

kursAdi = "Btk Akademi Python ile Programlama Dersleri"
website = "https://www.btkakademi.gov.tr/"

# 1- 'Btk Akademi ' karakter dizisinin baş ve sondaki boşluk karakterlerini siliniz*
#print(kursAdi.strip(' Btk Akademi '))

# 2- kursadi değişkenindeki tüm karakterleri küçük harfe çeviriniz
#print(kursAdi.lower())


# 3- website değişkeninde kaç tane '. 'karakteri vardır
#print(website.count('.'))

# 4- website değişkeni 'https' ilemi başlıyor
#print(website.startswith("https"))

# 5- web site 'tr' ile mi bitiyor?
#print(website.endswith("tr"))

# 6- kursAdi içerisindeki tüm karakterler harflerdenmi oluşuyor?
#print(kursAdi.isalpha())

# 7- kursadi değişkenindeki  tüm boşlukları '-' ile değiştirin
#print(kursAdi.replace(" ", "-").lower())

# 8- kursadi değişkenindeki  python kelimesini teactjs ile değiştitiniz
#print(kursAdi.replace("Python", "ReaxtJs"))

#  9-website değişkeni 'www' içeriyor mu* find()
#print(website.index("www")) bir değer bulamazsa hata dönderiri
#print(website.find("www")) bir değer bulumazssa -1 gönderiri

# 10- kursadi değişkenini listeye  ceviriniz
#print(kursAdi.split())