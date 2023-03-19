# import math

# 1.Funcție care să calculeze și să returneze suma a două numere
#
# a = int(input("Introdu primul numar:"))
# b = int(input("Introdu al 2-lea numar:"))
#
#
# def sum(numar1, numar2):
#     numar3 = numar1 + numar2
#     return numar3
#
#
# sum(a, b)
# print(sum(a, b))
# print("-----------------")
# numar_p_i = int(input("introdu un numar:"))
#
#
# def bool(numar_p_i):
#     if (numar_p_i % 2) == 0:
#         return (True)
#     elif (numar_p_i % 2) != 0:
#         return (False)
#
#
# print(bool(numar_p_i))
#
# print("--------------------")

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

# introduce_numele = input(str("introduce numele complet:"))
# print(introduce_numele)
# nume_string = introduce_numele.split(",")
# # nume_lungime = len(introduce_numele.strip(" "))
#
#
# def returneaza_numar():
#     for nume in nume_string:
#         if nume == print(len(introduce_numele)-introduce_numele.count(" ")):
#             return nume
#
#
# returneaza_numar()

print("--------------------")

# 4. Funcție care returnează aria dreptunghiului

# a = int(input("introduceti latimea: "))
# b = int(input("introdueti lungimea: "))
#
#
# def multiply(latime, adancime):
#     aria = int(latime*adancime)
#     return aria
#
#
# multiply(a, b)
#
# print(multiply(a, b))
#
# print("--------------------")
# 5. Funcție care returnează aria cercului

# r1 = float(input("introduceti raza cercului: "))
# import math
#
# def aria_cerc(r1):
#     a1 = math.pi*r1*r1
#     return a1
#
# print(aria_cerc(r1))
# aria_cerc(r1)
# print("--------------------")

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și Talse dacă nu găsește.
#
#
# str_input = str(input("introduce un string: "))
# no_hardcode = str(input("verifica daca se regaseste caracterul urmator: "))
#
# def returneaza_true(str_input):
#     for litera in str_input:
#         if str_input.__contains__(no_hardcode):
#             print(True)
#             return litera
#         else:
#             print(False)
#             return litera
#
#
# returneaza_true(str_input)
# print("--------------------")

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

# def exe7():
#     string = str(input("Introduce un string: "))
#     counter_lower_case = 0
#     counter_upper_case = 0
#     for letter in string:
#         if letter.islower():
#             counter_lower_case += 1
#         else:
#             counter_upper_case += 1
#     print("numarul de caractere mici este " + str(counter_lower_case))
#     print("numarul de caractere mari este " + str(counter_upper_case))

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive

# def positive_numbers(NumList):
#     Positive = []
#     for j in range(Number):
#         if (NumList[j] >= 0):
#             Positive.append(NumList[j])
#     return print("Elementele pozitive din lista sunt: ", Positive)
#
#
# NumList = []
# Positive = []
# j = 0
# Number = int(input("Va rog introduceti numarul total de elemente din lista: "))
# for i in range(1, Number + 1):
#     value = int(input("Va rog introduceti valoarea elementului %d: " % i))
#     NumList.append(value)
#
# positive_numbers(NumList)


# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

# def f9():
#     x = input("introduce prima valoare: ")
#     y = input("introduce a 2a valoare: ")
#     if x > y:
#         print("x este mai mare")
#     elif x < y:
#         print("y este mai mare")
#     elif x == y:
#         print("numerele sunt egale")
#
#
# f9()

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
# import random
#

# setul_meu = set(input("introduce un set:").split())
# user_input = (input("introduce un numar: "))


# def f10():
#
#     if setul_meu.__contains__(user_input):
#         print("nu am adaugat numărul în set. Acesta există deja")
#         return print(False)
#     elif int(user_input) not in setul_meu:
#         setul_meu.add(user_input)
#         print("Am adaugat numarul nou in set")
#         print(setul_meu)
#         return print(True)
#
#
# f10()
# print("Crowds cheering")
# print("Opening beer")

# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
# import datetime
#
# input_luna = int(input("va rugam introduceti o luna din an: "))
#
# def exe11():
#
