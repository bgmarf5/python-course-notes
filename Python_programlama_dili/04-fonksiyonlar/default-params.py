def selamlama(isim = " Kullanıcı ", mesaj = " İyi Günler "):# ikisinede default deger verebilir onemli olan ilk verinlen değer tek başına default değer verilmez karışır

    return f"{mesaj} {isim}"

sonuc = selamlama( "Ayşe BİLİT", "Merhaba")
sonuc = selamlama("Ali", " Selam")
sonuc = selamlama("Ali")
sonuc = selamlama()


def usAlma(taban,us = 2):
    return  taban ** us

sonuc= usAlma(2,3)
sonuc= usAlma(2)#burada da eğer sadece taban default alsaydı 2 hangi değere ait olduğunu bilemz
def toplam(a = 7 , b = 9):
    return a + b
def cikarma(a,b):
    return a - b
def islem(a,b):
    return toplam(a,b)
sonuc = islem(2,5)



def islem(a,b,fn=toplam):# 3. parametrede fonksiyon referansını göndererek kullanabilim
    return fn(a,b)
sonuc = islem(2,5,cikarma)

 
print(sonuc)




# KEYWORD ARGUMENTS( İSİMLENDİRİLMİŞ PARAMETRELER )
# def full_name(firstname,lastname):
#     return f" Your name is {firstname} {lastname} "
def full_name(firstname: str,lastname:str , age: int) -> str : # geri dönuş değerinide ->str string yapıyoruz
    return f" Your name is {firstname} {lastname} and your age {age} "
sonuc = full_name("Ayşe", "bilgi")
sonuc = full_name(lastname = "bilgi", firstname ="Ayşe")
sonuc = full_name(firstname="Ayşe", lastname="bidlgi", age=33)
print(sonuc)