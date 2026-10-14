# def selamlama(isim):
#     return "Merhaba " + isim

# print(selamlama("Sadık"))
# print(selamlama("Ayşe "))



# def toplam( sayi1, sayi2):
#     return sayi1 + sayi2

# print(toplam(133,344))
# print(toplam(1,4))

# def yashesapla(dogumyili):
#     return 2025 - dogumyili

# print(yashesapla(2000))
# print(yashesapla(2001))
# print(yashesapla(2002))


def yashesapla(dogumyili):
    return 2025 - dogumyili

def emeklikacyilvar(isim,dogumyili):
    yas = yashesapla(dogumyili)
    kalansure= 65 - yas

    if kalansure > 0:
        return f"{isim}, emekliliğinize {kalansure} yıl kaldı."
    else:
        return f" {isim}, zaten {abs(kalansure)} yıl önce emekli olmuşsunuz."
    


print(emeklikacyilvar("ayşa",2000))
print(emeklikacyilvar(" kandil", 2004))
print(emeklikacyilvar("osman", 1999))