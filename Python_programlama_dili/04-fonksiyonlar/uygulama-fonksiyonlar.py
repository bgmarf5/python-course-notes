#  1- Kendisine döderilen bir kelimeyi belirtilen  kez ekranda gösteren fonksiyonu yazınız.
def yazdir(text, adet):
    return text * adet

# print(yazdir(" Merhaba ", 5))
# 2- Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
#me
alan = 0
cevre = 0
def alan_cevre(kenar1, kenar2):
    alan = kenar1 * kenar2
    cevre = 2 *( kenar1 + kenar2)
    print(f"Dikdörtgenin alanı {alan} , çevresi {cevre} dir.")

#print(alan_cevre(12,24))
#ders

def hesapla(kisa, uzun):
    alan = kisa * uzun
    cevre = 2 * (kisa + uzun)

    return f"alan: {alan}  çevre: {cevre}"


sonuc = hesapla(12,14)
sonuc = hesapla(3,4)


print(sonuc)


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
def yazi_tura():
    import random
    sayi =random.random()
    
    if sayi< 0.5:
        return "Tura"
    else:
        return "Yazı"

#print(yazi_tura())

# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
# Me
def asal_sayilar(sayi1, sayi2):
    for asal in range(sayi1, sayi2):
        if ((asal % 2 != 0) and (asal % 3 != 0)):
            print(f" {asal} asaldır.") 
        else:
            print(f"{asal} Asal değildir")

#print(asal_sayilar(1,25))
def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if(sayi >1):
            for i in range(2, sayi):
                if(sayi % i == 0):
                    #break ile durdurulursa bu durumda else çalıştırılmaz
                    break
            else:
                print(sayi)

sonuc = asalSayilariBul(2,20)
print(sonuc)
    
#5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde dödüren fonksiyonu yazınız.
def tambolen(sayi):
    tamboleler = []
    for  i in range(2,sayi):
         if sayi % i == 0:
            tamboleler.append(i) 
    return tamboleler
print(tambolen(15))             
            


#print(tambolen(list(12)))




