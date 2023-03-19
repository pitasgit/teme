# Declară o listă note_muzicale în care să pui do re mi etc până la do ● Afișeaz-o
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)

# Inversează ordinea folosind slicing și suprascrie această listă. ● Printează varianta actuală (inversată)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)

# ● Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea.
# Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
# Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
note_muzicale.reverse()
print(note_muzicale)

# 2. De câte ori apare ‘do’?
print(note_muzicale.count("do"))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4] Găsește 2 variante să le unești într-o singură listă.

lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
lista_12 = lista_1 + lista_2
print(lista_12)
lista_123 = lista_1.__add__(lista_2)
print(lista_123)

# 4. ● Sortează și afișază lista generată la exercițiul anterior.
print(lista_12)
print(sorted(lista_12))

# ● Sortează numărul 0 folosind o funcție.

lista_12.remove(0)

# ● Afișaza iar lista.
print(lista_12)
# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază: ● Lista este goală. ● Lista nu este goală.

print(len(lista_12))

if len(lista_12) == 0:
    print("lista este goala")
else:
    print("lista nu este goala")

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.

lista_12.clear()
print(lista_12)

print(len(lista_12))

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.

if len(lista_12) == 0:
    print("lista este goala")
else:
    print("lista nu este goala")

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {"Ana": 8,
         "Gigel": 10,
         "Dorel": 5
         }

# Printează cei 3 elevi și notele lor Ex: ‘Ana a luat nota {x}’ Doar nota o vei lua folosindu-te de cheie

print(dict1.keys())
elev_1 = list(dict1.keys())[0]
nota_1 = str(dict1.get("Ana"))
print(elev_1 + ' a luat nota ' + nota_1)

elev_2 = list(dict1.keys())[1]
nota_2 = str(dict1.get("Gigel"))
print(elev_2 + ' a luat nota ' + nota_2)

elev_3 = list(dict1.keys())[2]
nota_3 = str(dict1.get("Dorel"))
print(elev_3 + ' a luat nota ' + nota_3)

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare

dict1["Dorel"] = 6
print(dict1.get("Dorel"))

# 11. Gigel se transferă din clasă ● Căuta o funcție care să îl șteargă
del dict1["Gigel"]
print(dict1)
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
dict1["Ionica"] = 9
print(dict1)

# 12. Set

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt
zile_sapt.add('luni')
print(zile_sapt)

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.

if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor saptamanii")
else:
    print("Weekend nu este un subset al zilelor saptamanii")

# 14. Afișează diferențele dintre aceste 2 seturi.
print(weekend.difference(zile_sapt))
print(zile_sapt.difference(weekend))

# 15. Afișază intersecția elementelor din aceste 2 seturi.

print(zile_sapt.intersection(weekend))

# Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:

lista_jucatori = ["Hagi", "Petre", "Luca", "Gica", "Mutu"]

schimbari_efectuate = 1
schimbari_max = int(3)
z = int(schimbari_max - schimbari_efectuate)
count = lista_jucatori.count("Luca")
print(lista_jucatori)
if count > 0 and schimbari_max > 0:
    print("efectueaza schimbarea")
    jucator_schimbat = lista_jucatori[2]
    lista_jucatori.remove("Luca")
    lista_jucatori.append("Adi Ilie")
    jucator_nou = lista_jucatori[4]
    print(f'A intrat in teren {jucator_nou}, a iesit {jucator_schimbat}, mai ai {z} schimbari')
elif count == 0:
    print(f'nu se poate efectua schimbarea deoarece jucatorul x nu e in teren')
    print(f'Mai ai {schimbari_max} schimbari')


