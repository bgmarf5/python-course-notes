

markalar = [ "opel", "bmw", "toyota"]

for marka in markalar:
    print(marka)


index =1
for marka in markalar:
    print(f"{index}-{marka}")
    index += 1
#enumerate bir class aracılığı iile bize gelen veriyi her bir elemanı indexliyor

obj1 = enumerate(markalar,1)
print(type(obj1))
print(list(obj1))


#
for marka in enumerate(markalar,1):
    print(marka)

#

for index,marka in enumerate(markalar,1):
    print(f"{index}-{marka}")



#zip
#iki listeyi eşleyip liste yaparken kullanılır döngü üzerinde kullanırız

numara=[100,200, 300]
ogrenci =["ali ","Ayşe ","canan ","Mehmet"]

print(list(zip(numara,ogrenci)))



for ogr in zip(numara,ogrenci):
    print(ogr)


for no,isim in zip(numara,ogrenci):
    print(no,isim)