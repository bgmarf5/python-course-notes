#mantıksal operatörler
#(yas >= 18) => true, false
#(mezuniyet == 'lise') ya da (mezuniyet == 'üniversite') => true, false
# sonuc = (yas >= 18) ve (mezuniyet == 'lise' ve ya mezuniyet == 'üniversite')

# And  = her bir koşul True olmalı   =   x > 5 and x < 10 

# OR  =  biri koşulun true olsa yeterli   =  x > 5 or x < 10

# Not  =  Sonucun tersini alır.   =  not( x > 5 and  x < 10 )


# Uygulama_mantıklsal_operatorler

# 1- Yaşı 18' den büyük  ya da  veli izni varsa bir işe çalışabilri durumunu kontrol ediniz
"""
yas = int(input("Yaşını giriniz : "))
izin =False
if (yas > 18) or (izin == True):# burada (izin) şeklindede kullanabiliriz
    print(f"Çalışabilir ")
else:
    print(f"çalışma durumuna uygun değil.")
"""
"""
# 2- Ders notu 50- 100 arasındaysa geçti değilse kalsın bilgisini yazdırınız
ders = int(input(" Ders notunu giriniz : "))
if ders > 50 and ders < 100 :
    print(f"dersten geçtiniz {ders}")
else:
    print(f"malesef dersten kaldınız {ders}")
"""

#  3- Not ortalaması en az 70 puan  ve zayıfı yoksa  teşşekür belgesi alabilme durumunu kontrol ediniz
"""not_ort = int(input("Not ortalamasını giriniz "))
# burada zayıf sayıs ını sorup sayıf sayısı 0 dan buyukse şeklinde şart koşabiliriz
if not_ort > 70  and not(not_ort < 70):
    print(f" Teşekkür belgesi almaya hak kazandınız. {not_ort}")
else:
    print(f" Teşekkür belgesi alamadınız. {not_ort}")"""

# 4- İşe girmek için en az  önlisans  ya da lisans mezunu  olma durumu kontrol  ediniz. sigara kullanma koşulu.
"""
sart = input("ne mezunu olduğunuzu yazın: ")
sigara_kullanim = False

if sart == " önlisans" or sart == "lisans" and sigara_kullanim == False:# and (not (sigara_kullanim)) şekklinde kullanılabilir
    print(f"Tebrikler işe alındınız. ")
else:
    print(f" Malesef işe alınamadınız. ")
"""

# 5- Uygulamaya giriş  kontrolünü "username yada email "  ve " parola " için yapalım.

username = "User"
email = "email@gmail.com"
parola="1234"

if ((username == input('username :')) or (email == input('email :'))) and (parola == input('parola :')):
    print(f"Başarıyla giriş yapmış bulunmaktasınız :")
else:
    print(f" Username, email veya parola yanlış tekrar deneyiniz.")