#uzun yol
"""sehirler = ['kocaeli', 'istanbul']
plakalar = [41, 34]

#key - value
print(plakalar[0], sehirler[0])#plakalardaki 0 değer sehirler0 a eşit bir
print(plakalar[1], sehirler[1])

print(plakalar[sehirler.index('istanbul')])
print(plakalar[sehirler.index('kocaeli')])
"""

#dictionary

plakalar = {
    'kocaeli': 41,
    'istanbul': 34,
    'izmir': 36
}
# liste üzerine eleman ekleme - güncelleme
plakalar['izmir'] = 35


print(plakalar['kocaeli'])
print(plakalar['izmir'])


#aşağıdaki öğrenci bilgilerini dictionary llistesinde saklayınız
    #101 yiğit bilgi  2010 (40, 80, 90)
    #102 Ada bilgi  2012 (80, 80, 80)
    #103 Çınar Turan  2017 (70, 70, 70)

ogrenciler = {
    101: {
        'ogrenci_numarasi': 101,
        'adi': 'Yiğit Bilgi',
        'dogum': 2025-2010,
        'not_ortalama': (40+80+90)/3
    },
    102 :{
         'ogrenci_numarasi': 102,
         'adi': 'Ada bilgi',
         'dogum': 2025-2012,#burayı çağırırken {2025- ogrenci["dogum"]} olarakta çağırabilirm
         'not_ortalama': (80+80+80)/3
    }

}
#print(ogrenciler)


# klavyeden girilen öğrenci numarasına göre aşagıdaki cümleyi yazdırınız
    # 101 numaralı yiğit bilgi ismindeki öğrencinin  yaşı 14 ve not oralaması 70
ogrenciNo = int(input('öğrenci no: '))
ogrenci = ogrenciler[ogrenciNo] # Burada gelen ogrenci noya göre ogrenciler nesnesinden ogrenci  bilgileri çağırdık
#ortalama = (ogrenci[not_ortalama][0] + ogrenci[not_ortalama][1] + ogrenci[not_ortalama][2]) / 3 
print(f"{ogrenciNo} numaralı {ogrenci["adi"]} ismindeki öğrencinin  yaşı {ogrenci["dogum"]} ve not oralaması {ogrenci["not_ortalama"]}")



# dictionary metotları


yemekTarifi = {
    "yemekadi": "Musakka ",
    "yemekTarifi": "tarif açıklaması",
    "resim": "1.jpg"
}

#access items
sonuc = yemekTarifi["yemekAdi"]
sonuc = yemekTarifi.get("yemekAdi")#burada yukarıdakinin metotla kullanımı
sonuc = yemekTarifi.keys()#dictionary içerisindeki anahtarları liste olarak veriri
sonuc = yemekTarifi.values()#buradada keyler umrumda değil değerleri liste olarak veriri
sonuc = yemekTarifi.items()#bütün dictionaru yapısını listeye çeviterek dönderiri

#upadate items
yemekTarifi["yemekAdi"] = "mantı"#hem güncelle hemde ekleme yapar 
yemekTarifi.update({"yemekadi":"manti"})
sonuc = yemekTarifi

# delete items
yemekTarifi.pop("yemekadi")
yemekTarifi.popitem()#listeye eklenen son itemi siler
yemekTarifi.clear()#bütğn listeyi siler
sonuc = yemekTarifi

print(sonuc)
