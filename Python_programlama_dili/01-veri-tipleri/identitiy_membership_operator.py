# is  = nesne benzerlihini kontrol eder  === x is y
# is not  ==== besbe benzerliğini  kontrol eder  ==== x is not y
# in   ==== listede varlık kontrolü yapar    ===== x in y
# not in  ==== listede varlık kontrolü yapar  x not in y

#  identity


x = [2,4,6]
y = [2,4,7]
z = y

print(x == y)
print(x is y) # nesnelerin karşılaştırma
print(x is not y)


print(z is y)
print(z is not y)

#  membership

print( 2 in x) # 2 x in içerisinde varmıdır
print(20 not in x)