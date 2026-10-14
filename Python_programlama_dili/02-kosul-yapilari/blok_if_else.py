"""email = "info@merhana.com"
parola = "123456"

if(email == "info@merhana.com"):
    if(parola == "123456"):
        print("Giriş başarılı")
    else:
        print("Parola yanlış.")
else:
    print("Mail adresininiz yanlış. ")"""




email = "info@merhana.com"
parola = "123456"

if(email != "info@merhana.com"):
    print("email yanlış")
elif(parola != "123456"):
    print(" Parola  yanlış. ")
else:
    print(" giriş yapıldı")



#soru
#soru
#diğer


x = 30
y = 30

if(x<y):
    print("x y den küçük")
elif(y < x ):
    print(" y x den küçüktür")
else:
    print(" x  y birbirine eşittir")


# Bir aracın yakıt tipine göre ( benzin, dizel, lpg ) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
benzin   = 39.35
dizel    = 41.71
lpg      = 20.28

mesafe  = int(input("Gideceğiniz mesafeyi giriniz:  "))
tip     = input("Alacağınız yakıt tipini  giriniz:  ")
if(tip == "benzin"):
    tutar = mesafe * benzin
    print(f" Ödenecek tutar {tutar}")
elif(tip == "dizel"):
    tutar = mesafe * dizel
    print(f" Ödenecek tutar {tutar}")
elif(tip =="lpg"):
    tutar = mesafe * lpg
    print(f" Ödenecek tutar {tutar}")
else:
    print(" Geçerli bir yakıt tipi giriniz. ")



# Hocanın çözümü
toplamYakitUcreti = 0
ortalamaYakitTuketimi = float(input("100 km' deki ortalama yakıt tüketimi: "))
gidilecekYol = float(input("Gidilen mesafe :"))
yakitTipi = input(" Yakıt Tipi:  ")

toplamyakitTüketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)


if(tip == "benzin"):
    toplamYakitUcreti = benzin * toplamyakitTüketimi
    print(f" Ödenecek tutar {toplamYakitUcreti}")
elif(tip == "dizel"):
    toplamYakitUcreti = dizel * toplamyakitTüketimi
    print(f" Ödenecek tutar {toplamYakitUcreti}")
elif(tip =="lpg"):
    toplamYakitUcreti = lpg * toplamyakitTüketimi
    print(f" Ödenecek tutar {toplamYakitUcreti}")
else:
    print(" Geçerli bir yakıt tipi giriniz. ")






# Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığınıa karşılık gelen değerlendirmeyi yazdırınız.

# 0 - 24  => 0
# 25 - 44  => 1
# 45 - 54  => 2
# 55 - 69  => 3
# 70 - 84  => 4
# 85 - 100  => 5

not_1 = int(input("1. notu giriniz : "))
not_2 = int(input("2. notu giriniz : "))
soz = int(input(" Sözlü notunu giriniz : "))

ort = (not_1 + not_2 + soz) / 3

if(ort < 25 and ort > 0):
    print(f" Ortalamanız {ort}. Değerlendirme notu 5 üzerinden 0")
elif(ort < 45 and ort > 24):
    print(f"Ortalamanız {ort}. Değerlendirme notu 5 üzerinden 1")
elif(ort > 44 and ort < 55):
    print(f"Ortalamanız {ort}. Değerlendirme notu 5 üzerinden 2")
elif(ort > 54 and ort < 70):
    print(f"Ortalamanız {ort}. Değerlendirme notu 5 üzerinden 3")
elif(ort > 69 and ort < 85):
    print(f"Ortalamanız {ort}. Değerlendirme notu 5 üzerinden 4")
elif(ort > 84 and ort < 101):
    print(f"Ortalamanız {ort}. Değerlendirme notu 5 üzerinden 5")
else:
    print(f" Tekrar deneyiniz. ")

