# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except ZeroDivisionError:
#     print("y sıfır olamaz.")
# except ValueError:
#     print("x ve y sayı olmalıdır.")
# except:
#     print("bilinmeyen hata oluştu.")


# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except (ZeroDivisionError, ValueError) as ex: # loglamak  için as ex
#     print("x ve y sayı olmalıdır, y sıfır olamaz.")
#     print(ex)
# except Exception:
#     print("bilinmeyen hata oluştu.")

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x / y)
    except (ZeroDivisionError, ValueError) as ex: # loglamak  için as ex
        print("x ve y sayı olmalıdır, y sıfır olamaz.")
        print(ex)
    except Exception as e:
        print("bilinmeyen hata oluştu.")
        print(e)
    else:
        break
    finally:
        print("finally bloğu çalıştı.")

