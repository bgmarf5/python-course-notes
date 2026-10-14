"""
    Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.

    Kullanımı          :   open(dosya_adi, dosya_erişme_modu )
    dosya_erişme_modu  :   dosyayı hangi amaçla açtığımızı belirtir.
    "r" okuma modu     :   okuma modu. belirtilen konumda dosya olmalıdır.
    seek(aramak)       :   cursor konumu
"""

# f = open("log.txt")# log.txt dosyası bulunmalı

# print(f)

f = open("log.txt",encoding = 'utf-8')

print(f.read())
print(f.read())
#f = open("log.txt",encoding = 'utf-8') terminalde açarken
#f.read() dosya içerisini okuruz
#f.seek(0) cursoru en başa getirir
#f.readline() terminalde satır satır sırayla getirir
# f.readlines() butun satırları bize bir liste halinde verir
# satirlar =f.readlines()bu sayede satirlar üzreinden listeye ulaşırız
#f bizim objemiz 
#f.colsed  kapalı olum olmadığına bakar kaplıysa true\ açıkise false
#f.close()objemizi kapatır. bundan sonra işlem yapamayız