# Faktöriyel fonksiyonu oluşturunuz ve fonksiyona gelen değer için hata mesajları verin.


# def faktoriyel(deger):

#     deger = int(deger)
#     if (deger<0):
#         raise ValueError("Negatif değer")
#     sonuc = 1

#     for i in range(1, deger + 1):
#         sonuc *= i
#     return sonuc
# for i in [3,6,7,'2a',-1, -6, 9]:
#     try:
#         deger = faktoriyel(i)
#     except ValueError as e:
#         print(e)
#         continue
#     else:# herhangi bir except çalışmazsa else çalışır
#         print(f"{i} nin faktöriyeli {deger} dir.")



# 2- Girilen parola içinde türkçe karakter hatası veriniz
def parolakontrol(parola):
    turkçe_karakterler = "şçğüöİ"

    for i in parola:
        if i in turkçe_karakterler:
            raise TypeError("parola türkçe karakter içeremez")
        
    print("Geçerli parola")

parola = input("parola:  ")

try:
    parolakontrol(parola)
except TypeError as e:
    print(e)