#"W" : (Write) yazma modu
#   ** Dosyayı konumda oluşturur
#   ** Eğer konumda aynı dosya varsa dosyayı  siler ve yeni oluşturur

# file = open("dosya.txt","w",encoding='utf-8')
# file.write("merhabalar\n")
# file.write("naber müdür\n")
# file.close()

#with ile dosay.txt yazdık ve okuduk 
with open("dosya.txt","w",encoding='utf-8') as file:
    file.write("merhabalar\n")
    file.write("naber müdür\n")

with open("dosya.txt","r",encoding='utf-8') as file:
    for i in file:
        print(i, end="")