# open(dosya_adi, dosya_erişim_modu)
# dosya_erişim_modu => dosyayı hangi amaçla açtığımızı belirtir



# "r": (Read) okuma. Dosya konumda yoksa hata verir.
# "w": (write) yazma modu.
#   ** Dosyayı konumda oluşturur.
#   ** Dosya içeriğini siler ve yeniden ekleme yapar
# "a": (Append) ekleme. Dosya konumda yoksa  oluşturur.
# "r+": Hem okuma hem yazma modunda açılır( cursoru hareket ettirebilirsin ). Dosya konumda yokda hata verir.


# with open("dosya.txt","r+", encoding="utf-8") as file:
#     file.seek(0)
#     file.write("eski satir\n")# burada cursor 0 a doner ve var olanın üzerine yazar


with open("dosya.txt","r+", encoding="utf-8") as file:
    #file.seek(0)
    #file.read()#appendin işlevseliğini read() çalıştırarak cursorun en sona alınmasını sağlanılabilir
    print(file.read())
    file.write("son satir\n") 