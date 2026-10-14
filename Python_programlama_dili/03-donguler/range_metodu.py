#liste = [ 1,2,3,4]

#for i in liste:# burada liste ye mutlaka ihtiyac duyarız range içerisinde boyle bir ihtiyacı engeller
    #print(i)

#for i in range(1, 100, 2):# start, stop , step = start dahil stop -1 i
#   print(i)


rng = range(10)
rng = range( 10, 20)
rng = range( 100,200,10)
rng = range(0, -20, -3)

sonuc =list(rng)
print(sonuc)


for i in range(50, 200):
    if(i % 2==0):
        continue
    print(i)

for i in range( 200, 100,-2):
    if(i % 2==0):
        print(i)