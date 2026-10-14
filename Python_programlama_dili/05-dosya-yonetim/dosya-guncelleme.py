# with open("markalar.txt","a") as file:
#     file.write("7-Ford")
# with open("markalar.txt","r+",encoding="utf-8") as file:
#      markalar = file.read()
#      markalar = "1-Toyota\n" + markalar
#      file.seek(0)
#      file.write(markalar)
# # # Yukarısı okur ve dosyaya ilk satırına yazar 
# # # Aşağısı ekrana yazdırır
# with open("markalar.txt","r",encoding="utf8") as file:
#      print(file.read())

# Herhangi bir satıra ekleme
with open("markalar.txt","r+",encoding="utf-8") as file:
    markalar = file.readlines()
    markalar.insert(4,"5-Maza\n")
    file.seek(0)
    # for marka in markalar:
    #     file.write(marka)
    file.writelines(markalar)#writelines bizden dizi bekler


with open("markalar.txt","r",encoding="utf-8") as file:
    print(file.read())