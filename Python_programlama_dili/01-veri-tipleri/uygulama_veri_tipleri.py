"""
    Uygulama 1: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınz.
    alan:nr2
    çevre: 2nr

    uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplıyınız
    mil = km / 1.609344
"""

#uygulama 1
r=4
pi=3
alan = pi * (r**2)
cevre = 2 * pi * r
print("Alanı:"+ str(alan))
print("Çevre : "+ str(cevre))

#uygulama 2
km =float(input("km bilgisini giriniz. "))
mil=km / 1.609344
print(str(km)+"mil cinsinden değeri:  "+  str(mil))