import module

sonuc = module.sayi
sonuc = module.sayilar
sonuc = module.urun
sonuc = module.urun["urunAdi"]
sonuc = module.toplama(23,54)


import module as m
sonuc = m.sayilar


from module import sayi, sayilar, urun
sonuc = sayi
sonuc = sayilar
sonuc = urun


from module import*
sonuc = urun
sonuc = toplama(23,55)

print(sonuc)