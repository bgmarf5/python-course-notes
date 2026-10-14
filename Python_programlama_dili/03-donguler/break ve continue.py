# for üzerinde break ve continue  kullanım

isim = "Ahmet Hamdi"

for harf in isim:
    if( harf== "t"):
        continue
    print(harf)




for harf in isim:
    if (harf == "t"):
        break
    print(harf)


# while üzerinde break  ve continue

i = 0

#while( i < 5):
   # i += 1
    #if(i % 2 == 1):
     #   continue
    #print(i)

while( i < 5):
    i += 1  # break komutundan sonra koymamızın sebebi döngünün devam etmesi için
    if(i == 3):
        break
    print(i)


while( i < 5):
    i += 1  # break komutundan sonra koymamızın sebebi döngünün devam etmesi için
    if(i == 3):
        continue
    print(i)

s = 0
toplam = 0

while ( s <= 100):
    s += 1
    if( s % 2 == 0):
        continue
    toplam += s

print(s)





