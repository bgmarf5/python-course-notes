#sets indekslenemez, liste elemanları sıranalamas, güncellenemez, elemeanlar tekrarlanamaz, elemean siler yada ekleriz
#meveler={"elma","armut","kiraz"}

meveler={"elma","armut","kiraz"}

for x in meveler:
    print(x)

sonuc = "elma" in meveler # elma meveler listesinde varmı kontrol ediliyor boolean türü
meveler.add("karput")
meveler.update()
#remove discard silme yapar birde pop ve clear var
sonuc = meveler
print(sonuc)
 

#value referans tipleri
#value types
x = 10
y = 20

x = y
print(x,y) # ikisinide 20 olarak yazar


#referance
 
a = ["elma", "armut"]
b = ["elma", "armut"]

a = b# adresleri eşitliyoruz adres kopyaladınız
a[0] = "üzüm"

print(a,b)

#liste kopalama
listeA = [10,20]
#listeB = listeA.copy() # 1.yöntem
listeB = list(listeA) # 2.yöntem listea yı list metodu ile cevirip listebye atıryorz


listeB[0] = 30

print(listeA, listeB)