import sqlite3

connection = sqlite3.connect("deneme.db")

cursor =connection.cursor()

sql = "INSERT INTO geres(name) Values('Macera')"
cursor.execute(sql)
connection.commit()


# cursor.execute("select * from customers")#select * from customlers where city ='Oslo'
# result = cursor.fetchall()# fetchall geriue liste donürür buyuzden dongu kullanırız
# result= cursor.fetchone()# tek bir değer döndürürü dongu kullanmayız tek ir kayıt gelir


# for customer in result:
#     print(customer[0] +" " + customer[2])

connection.close()
print("veri tabanı bağlantısı hazır.")