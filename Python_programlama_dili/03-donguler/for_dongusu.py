# for ==> list

sayilar = [1,2,3,6,5,7,8,77,76,99]
isimler = ["Ali", "Veli", "Deli"]
adsoyad = " Buğlem Demir"

for x in sayilar:#sayılar listesindeki elemanları x e geçici atar tek tek yazdırır.
    print(x)

for x in sayilar:
    print("Merhabalar.") # sayilar listesinin elemanı kadar merhabalar yazdırır.

for isim in isimler:# isimler listesindeki elemanları alt alta yazdırır
    print(isim)

for i in adsoyad:
    print(i)

#tuple da for kullanımı
my_tuple = [(1,2),(4,5),(6,7)]


for i in my_tuple:
    print(i)


for a,b in my_tuple:
    print(a,b)



# dictinory ile kullanımı

my_dict = {"41":"Kocaeli", "53":"Rize","35":"İzmir"}

for x in my_dict:
    print(x)# x bize listenin key bilgilerini verir


for x in my_dict:
    print(my_dict[x])# value değerini verir


for x in my_dict.values():#bu bize direkt listenin value değerlerini verir
    print(x)  

for x in my_dict.keys():#listenin direkt keys değerlerini verir
    print(x)

for x,y in my_dict.items():# key ve value değerlerini birlikte liste olarak verir
    print(x,y)