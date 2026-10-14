# 1- "toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz
markalar =["Toyota","BMW","Renault","Mercedes"]

# 2- Liste kaç elemanlıdır
#sonuc =len(markalar)

# 3- Listenin ilk ve son elemanı nedir?
#sonuc = markalar[0]
#print(sonuc)
#sonuc = markalar[-1]
#print(sonuc)


# 4- "Renault" markasını "Togg" ile güncelleyiniz
#markalar[-2] = "Togg"
#sonuc = markalar
#print(sonuc)

# 5- "togg" listenin bir elemanımıdır?
#sonuc = "Togg" in markalar
#sonuc = "Togg" not in markalar elemanı değilmi demek
#print(sonuc)


# 6- listenin ilk 2 elemanını alnız
#sonuc =markalar[:2]
#print(sonuc)

# 7- listenin sonuna "ford"  ve "citroen" markalarını ekleyiniz
#sonuc = markalar +[ " ford " , " citroen "]
#print(sonuc)


# 8- listenin son elemanını siliniz
#del markalar[-1]
#print(sonuc)


# 9- Aşağıdaki verileri liste içerisinde saklayınız
ogrenci_1 =["yiğit "," Bilgi ", 2010,[ 70, 80, 90 ] ]
ogrenci_2 =["Ada ", "Bilgi ", 2011,[70, 70, 80]]
ogrenci_3 =["Çınar ", "Turan ", 2017,[60, 60, 90]]

ogrenciler =[ogrenci_1, ogrenci_2, ogrenci_3]
# 10- öğrencilerin yaşlarını hesaplayınız
yasy = 2025 -ogrenci_1[2]
yasa = 2025 -ogrenci_2[2]
yasc = 2025 -ogrenci_3[2]
print(yasy, yasa, yasc)


# 11- öğrencilerin not ortalamalarını hesaplayınız
notyiğ = (ogrenciler[0][3][0] + ogrenciler[0][3][1] + ogrenciler[0][3][2]) / 3
notada = (ogrenciler[1][3][0] + ogrenciler[1][3][1] + ogrenciler[1][3][2]) / 3        
notcin = (ogrenciler[2][3][0] + ogrenciler[2][3][1] + ogrenciler[2][3][2]) / 3

print(notyiğ, notada, notcin)