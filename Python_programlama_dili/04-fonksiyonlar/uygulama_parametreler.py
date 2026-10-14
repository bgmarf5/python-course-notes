# Bankamatik Uygulaması

# Hesap bilgileri tutulacak. (dict)
# Menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# Çekilmek istenen tutar hesapta yoksa ek hesabın  kullanılmak istendiği sorulacak


hesaplar = [
    {
        "ad":"Sadık Turan",
        "hesapNo": "12345",
        "bakiye": 20000,
        "ekHesap": 5000,
        "username":"Sadikturan",
        "password": "1234"
    },
    {
        "ad":"Ali veli",
        "hesapNo": "12375",
        "bakiye": 1000,
        "ekHesap": 2000,
        "username":"ali",
        "password": "1"
    }
]

def menu(hesap):
    print("\n")

    print(f"Merhaba, {hesap["ad"]}")


    print("1- Bakiye sorgulama")
    print("2- Para çekme")
    print("3- Para Yatırma")

    islem = input("Yapmak istediğiniz işlem:")

    print("\n")
    
    if islem == "1":
        bakiyesorgulama(hesap)
    elif islem == "2":
        paracekme(hesap)
    elif islem == "3":
        parayatirma(hesap)
    else:
        print("Yanlış bir işlem seçtiniz")
    
    menu(hesap)
    





def bakiyesorgulama(hesap):
    print(f"Bakiyeniz : {hesap["bakiye"]} TL dir")
    print(f"Ek Hesap Bakiyeniz : {hesap["ekHesap"]} TL dir")


def paracekme(hesap):
    tutar = int(input(" Çekmek istediğiniz tutar giriniz :"))
    
    
    if hesap["bakiye"] >= tutar:
        hesap["bakiye"] -= tutar
        print(f"Paranızı alabilirsiniz")
        
    elif hesap["bakiye"] <= tutar:
        ekhesapkullanimIzni = input("Ek hesap kullanılsınmı (e/h):")
        if ekhesapkullanimIzni == "e":
            kullanilacakMiktar = tutar - hesap["bakiye"]
            hesap["bakiye"] = 0
            hesap["ekHesap"] -= kullanilacakMiktar
            print("Paranızı alabilirsiniz")
        else:
            print(" yetersiz bakiye")


def parayatirma(hesap):
    parayatir = int(input("Yatırmak istediğiniz tutarı giriniz: "))

    hesapsec = input("Hangi hesaba yattıracağınızı seciniz (hesap = H / ekhesap = E)")
    print("\n")
    if hesapsec == "H":
        hesap["bakiye"] += parayatir
        print("Paranız başarıyla yatırılmıştır. ")
    elif hesapsec == "E":
        hesap["ekHesap"] += parayatir
    else:
        print(" Geçersiz işlem yapılmıştır.")


def login():
    usernam = input("Kullanıcı adınızı giriniz.")
    pswrd = input("Şifrenizi giriniz.")

    isLoggedIn = False

    for hesap in hesaplar:
        if usernam == hesap["username"] and pswrd == hesap["password"]:
            isLoggedIn = True
            menu(hesap)
            break

    if not(isLoggedIn):
        print("Username yada parola yanlış")



login()