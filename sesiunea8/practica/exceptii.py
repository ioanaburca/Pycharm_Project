# Exceptii in Python

# Exemplul 1:
# x = 5 / 0  # ZeroDivisionError

# Exemplul 2:
# my_dict = {'pret': 25.00, 'nume': 'perna'}
# print(my_dict['culoare']) # KeyError

# try:
#     x = 5 / 0
# except ZeroDivisionError:
#     print("Can not divide by zero!")

# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Al doilea parametru trebuie "
#                                 "sa fie diferit de 0.")
#     return a / b
#
# print(divide(1, 0))


# Nu e o practica recomandata
# Ne dorim sa prindem exceptii specifice si sa le prelucram separat
# try:
#     x = 5 / 0
# except Exception:
#     print("Can not divide by 0.")


# In blocul try avem mai multe exceptii
# In except -> vrem sa prindem fiecare exceptie in parte si sa o prelucram
# separat.

def my_func(y, key):
    try:
        x = 5 / y # ZeroDivisionError
        my_dict = {'pret': 25.00, 'nume': 'perna'}
        print(my_dict[key]) # KeyError
    except ZeroDivisionError:
        return 0
    except KeyError:
        print("Key is not present in dict")

print(my_func(0, 'pret'))
# my_func(2, 'culoare')