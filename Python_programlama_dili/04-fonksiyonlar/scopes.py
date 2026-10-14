# local scope(kapsam)
# global scope


# x = "global scope"

# def my_funch():
#     x = "local scope"
#     print(x)

# my_funch()
# print(x)

#----------------------------------------------

# name = "Çınar"

# def change_name(new_name):
#     name = new_name
#     print(name)

# change_name("Ada")
# print(name)


# name = "Elma"

# def change_name(new_name):
#     global name
#     name = new_name
#     print(name)

# change_name("Armut")
# print(name)

#---------------------------------------
# iç içe fonks
# en içten dışa doğru seçilir

# name = "global string"

# def greeting():
#     name = "Çınar"

#     def hello():
#         #name = "Ada"
#         print("hello ", name)

#     hello()

# greeting()
#----------------------------------------


x = 50

# def test(x):
#     print(f"x: {x}")

#     x = 100
#     print(f"changed x to {x}")

# test(x)
# print(x)

def test():
    global x
    print(f"x: {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)