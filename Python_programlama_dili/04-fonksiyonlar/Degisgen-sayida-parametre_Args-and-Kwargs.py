#args kullanımı fazla parametre ilede toplama işlem yapmamı sağlar

# sayilar = (10,20,40,33)

# def toplam(liste):
#     sonuc = 0
#     for i in liste:
#         sonuc += i
#     return sonuc

#sonuc = toplam(sayilar)

# def toplam(*args):# dışarıdan args parametresi alsın (*)args bir değişken sayıda parametresi olduğunu soyler
#     print(args)
#     print(type(args))
#     sonuc = 0
#     for i in args:
#         sonuc += i
#     return sonuc
# #sonuc = toplam(10,30)
# sonuc = toplam(20,40,4,44)
# print( sonuc )

#kwargs  dict yapısında gelicek

# def display_user(*args):
#     print(type(args))
#     print(args)


# display_user()

# def display_user(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# display_user()


def display_user(**kwargs):
    # print(type(kwargs))
    # print(kwargs)

    for key,value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")

display_user(username = "Melike melek")
display_user(username = " Meliek seline", email ="infokalem@gmail.ccom")
display_user(username= "melek seleam", email = "infokalem@gmail.com", country = "Türkiye")

def myFunc(a,b,c,*args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40, 50, 60,key1 = "value", key2 = "value 2")
      