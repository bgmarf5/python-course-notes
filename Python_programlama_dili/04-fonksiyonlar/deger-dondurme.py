def toplam():
    return 10 + 38

sonuc = toplam()

#print(sonuc)

def yil():
    import datetime
    return datetime.datetime.now().year


def saat():
    import datetime
    return datetime.datetime.now().hour

def yasHesapla():
    return yil()- 1982

print(yasHesapla())


def selamla():
    if(saat()< 12):
        return " Günaydınn"
    else:
        return"Saat cok geç olmuş"
    
print(selamla())