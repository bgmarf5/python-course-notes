customers = ["sadikturan ", "ahmetyilmaz", "cinarturan", "yiğitbilgi"]
order_totals = [12000, 13000, 5000, 15000]

# 1- 'sadikturan' kullanıcı adıyla yapılan 5000 liralık  siparişi listeye ekleyiniz.
customers.append("sadıkturan")
order_totals.append(8000)


# 2- son eklenen siparişi siliniz.
customers.pop()
order_totals.pop()



# 3- tüm müşteriler için aşağıdaki özet cümleyi yazdırınız
#username isimli müşterinin siparişi toplamı 100 liradır
print(f"{customers[0]} isimli müşterinin sipariş toplamı {order_totals[0]} liradır")


# 4- müşterileri alfabetik olarak sıralayınız
customers.sort()
print(customers)


# 5- sipariş toplamlarını azalan şekilde sıralayınız
order_totals.sort()
order_totals.reverse()

print(order_totals)


# 6- en düşük sipariş hangisidir
min =min(order_totals)
print(min)

# 7- 'sadıkturan' isimli kullanıcının kaç tane siparişi vardır

sira=customers.count('sadikturan')
print(sira)

# 8- customers listesinden ahmetyilmaz isimli kullanıcıyı siliniz
customers.remove('ahmetyilmaz')
print(customers)

# 9- listelerdeki tüm içerikleri siliniz
customers.clear()
order_totals.clear()

# 10- kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarıını listeye ekleyinz
kullanici =input("kullanıcı adını giriniz :")
siparis_top = int(input("lütfen sipariş toplamını giriniz"))

customers.append(kullanici)
order_totals.append(siparis_top)
print(customers)
print(order_totals)