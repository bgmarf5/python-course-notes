#for => list
sayilar = [1,2,3,4,5,6,7,8,9]
# while  => koşullu , kod bloğunu defalarca çalışması için


while True:
    print("koşul sürekli true olduduğu mudetçe çalışmaya devam eder")
    break

i = 0

while i <10:
    print(i)
    i += 1

i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1