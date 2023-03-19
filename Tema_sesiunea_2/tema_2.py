# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
# if else executa atat partea adevarata a unei conditii, cat si partea falsa a acesteia.
# daca conditia este adevarata, se printeaza if, daca conditia este falsa, se printeaza else
import math
import random

# 2. Verifică și afișează dacă x este număr natural sau nu.
x = 11
if x >= 0 and type(x) == int:
    print('numarul x este numar natural')
else:
    print('numarul x NU este natural')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
if x > 0:
    print('x este pozitiv')
elif x < 0:
    print('x este negativ')
else:
    print('x este neutru')

# 4. Verifică și afișează dacă x este între -2 și 13.
if -2 < x < 13:
    print('numarul se afla intre -2 si 13')
else:
    print('numarul NU se afla intre -2 si 13')

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
y = 11
if x-y < 5:
    print('diferenta intre x si y este mai mica de 5')
else:
    print('diferenta intre x si y NU este mai mica de 5')
# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.

if not 5 < x < 27:
    print('x NU se afla intre 5 si 27')
else:
    print('x se afla intre 5 si 57')
# 7. x și y (int) Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare

if int(x) == int(y):
    print('x si y sunt egale')
elif int(x) > int(y):
    print('x este mai mare')
else:
    print('y este mai mare')

# 8. X, y, z - laturile unui triunghi. Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
z = 6
if x == y == z:
    print('triunghiul este echilateral')
elif x == y and x >= z and y >= z:
    print('triunghiul este isoscel')
else:
    print('triunghiul este oarecare')

# Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu
litera = 'B'
if (litera == 'A' or litera == 'a' or litera == 'E' or litera == 'e' or litera == 'I'
        or litera == 'i' or litera == 'O' or litera == 'o' or litera == 'U' or litera == 'u'):
    print("litera este vocala")
elif(litera == 'B' or litera == 'C' or litera == 'c' or litera == 'D'
     or litera == 'd' or litera == 'G' or litera == 'g' or litera == 'H' or litera == 'h' or litera == 'J'
     or litera == 'j' or litera == 'K' or litera == 'k' or litera == 'L' or litera == 'l' or litera == 'M'
     or litera == 'n' or litera == 'P' or litera == 'p' or litera == 'Q' or litera == 'q' or litera == 'R'
     or litera == 'r' or litera == 'S' or litera == 's' or litera == 'T' or litera == 't' or litera == 'V'
     or litera == 'v' or litera == 'W' or litera == 'w' or litera == 'X' or litera == 'x'
     or litera == 'Z' or litera == 'z'):
    print("litera este consoana")
else:
    print('litera citita este nu este tip litera')


# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A Peste 8 => B Peste 7 => C Peste 6 => D Peste 4 => E 4 sau sub => F
nota_ro = 7.8
nota = int(nota_ro.__round__())
if nota <= 4:
    print('nota este F')
elif 4 > nota < 6:
    print('nota este E')
elif 6 >= nota < 7:
    print('nota este D')
elif 7 >= nota < 8:
    print('nota este C')
elif 8 >= nota < 9:
    print('nota este B')
else:
    print('nota este A')  # aici am incercat sa pun limita la 10 dar nu m-am descurcat

# 1.Verifică dacă x are minim 4 cifre (x e int). (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# 2.Verifică dacă x are exact 6 cifre.
x = 57667
digits = int(math.log10(x)+1)
print(digits)
if digits >= 4 and digits != 6:
    print('numarul cifrelor in x este minimum 4')
elif digits == 6:
    print('numarul cifrelor din x este 6')
else:
    print('numarul cifrelor in x este mai mic decat 4')
# 3.Verifică dacă x este număr par sau impar (x e int).
if x % 2 == 0:
    print('x este par')
else:
    print('x este impar')

# 4. x, y, z (int) Afișează care este cel mai mare dintre ele?

x = int(4)
y = int(6)
z = int(5)

if x <= y < z:
    print('z este cel mai mare')
elif x > y >= z:
    print('x este cel mai mare')
elif x < y > z:
    print('y este cel mai mare')
else:
    print('valoare invalida')

# 5. X, y, z - reprezintă unghiurile unui triunghi Verifică și afișează dacă triunghiul este valid sau nu.

if x > 0 and y > 0 and z > 0:
    print('triunghi valid')
else:
    print('triunghi invalid')

# Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citiți de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

prop = 'Coral is either the stupidest animal or the smartest rock'
x = 23
prop_str = prop[:-x:]
print(prop_str)

# 7.Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5

prop_5 = prop[:5]+prop[-5:]
print(prop_5)

# 8. Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock
# (hint: este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest cuvant
# ● output: 'Coral is either the stupidest animal or the smartest '
index = prop.index('rock')
print(index)
varstr = prop[0:index]
print(varstr)

# 9. Citește de la tastatura un string
# Verifică dacă primul și ultimul caracter sunt la fel.
# Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat

cat = "Acesta este un string"
assert cat[0] != cat[-1]  # nu inteleg daca trebuie sa il las asa sau sa il egalizez? sunt un pic derutat

# Avand stringul '0123456789'
# ● Afișați doar numerele pare
# ● Afișați doar numerele impare (hint: folositi slicing, controlați din pas)

numar = '0123456789'
print(numar[::2])
print(numar[1::2])

# 11. Joc ghicit zarul
dice_roll = random.choice([1, 2, 3, 4, 5, 6])
print(dice_roll)

user = 4

if user < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {user} dar a fost {dice_roll}')
elif user > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {user} dar a fost {dice_roll}')
elif user == dice_roll:
    print(f'Ai ghicit. Felicitari! Ai ales {user} si zarul a fost {dice_roll}')
