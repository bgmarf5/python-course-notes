a, b, c = 4, 8, (12, 2)

# 1- kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir ?
"""toplam =+ (a, b, [c])
sayi_1 = int(input("1. sayıyı giriniz :"))
sayi_2 = int(input("2. sayıyı giriniz :"))
carpim = sayi_1 * sayi_2
toplam = a + b + (c[0] + c[1])
sonuc = carpim - toplam
print(sonuc)"""
"""
# 2-c nin b ye kalansız bölümünü hesaplayınız
sonuc = (c[0] + c[1]) // b
print(sonuc)

# 3- (a,b,c) toplamının  mod  7 si nedir
toplam = a + b + (c[0] + c[1])
mod = toplam % 7
print(mod)

#  4- b inin a. kuvvetini hesaplayınız
b**=a
print(b)

# 5- a, *b, c = (2,4,6,8,13) işlemine göre c nin  küpü nedir
a, *b, c = (2,4,6,8,13) # a =2 c =13 *b= eşitlenenler hariç hepsi b ye eşitlenir
kup = c**3
print(kup)
# 6- a,b, *c = (2,4,6,8,13) işlemine göre c nin değerleri toplamı nedir
a,b, *c = (2,4,6,8,13)
# a = 2 b=4 c= 6,8,13
print(c)
toplam = (c[0] + c[1] + c[2])
print(toplam)"""


#karşilaştırma operatörleri
"""eposta = "info@sadikturan.com"
prola = "135690"

sonuc = (eposta == input('eposta: '))#bu şekilde kullanıcıya soruduğumuz soruyla işlem yapabiliyoruz
sonuc = (prola == input('parola : '))# burada kullanıcın yazdığı parola praolayla eşitse true değilse false döner
print(sonuc)

#karşılaştırma operatorl
a,b,c,d = 2,3,10,5


sonuc = (a == c)
print(sonuc)"""



# 1- Girilien 2 sayıdan hangisi büyüktür ?
"""sayi_1 = int(input("1. Sayıyı giriniz :"))
sayi_2 = int(input("2. sayıyı giriniz: "))
if sayi_1 > sayi_2:
    print(sayi_1)
else:
    print(sayi_2)"""

"""
# 2- Girilen bir sayının tek çift kontrolünü yapınız
sayi = int(input("Sayı giriniz : "))
if sayi % 2 == 0:
    print("çift")
else:
    print("tek")
"""

# 3- Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz. 50 ve üstünde başarılı
not_1 = int(input("1. Sayıyı giriniz :"))
not_2 = int(input("2. Sayıyı giriniz :"))
not_3 = int(input("3. Sayıyı giriniz :"))

ort =(not_1 + not_2 + not_3) / 3

if ort > 50 :
    print(f"başarılı{round(ort,2)}")
else:
    print(f"başarısız {ort}")