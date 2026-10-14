# file = open("log.txt",encoding='utf-8')

# print(file.read())

# file.close() 
# with ile file.close() gerek kalmayıp as file ile referans alabilirsiniz

# with open("log.txt", encoding='utf-8') as file: # with  kapsamından çıktıktan sonra kendi kapanır
#     for i in file:
#         print(i, end ="")#end="" boşluğun okunmasını iptal için
    # print(file.read(8))
    # print(file.tell())
    # print(file.read())
    # print(file.tell())

#print(file.read(10)) 10. karaktere kadar oku
#print(file.tell()) tell cursor nerede onu soler
try:
    with open("log2.txt", encoding='utf-8') as file:
        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print(" Dosya okuma hatası.")

# Bir hata objesini ele almak için try:execpt kullanıyoruz 
