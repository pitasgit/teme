# # 1.Având lista:
#
import random

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

#
# # Folosește un for că să iterezi prin toată lista și să afișezi;
# # ● ‘Mașina mea preferată este x’.
# for masina_preferata in range(len(masini)):
for masina_preferata in masini:
    if masina_preferata == 'Mercedes':
        print(f'Masina mea preferata este {masina_preferata}')
              # + str(random.choice(masini)))
print('---')
# # ● Fă același lucru cu un for each.
for masina_preferata in masini:
    print(f'Masina mea preferata este {masina_preferata}')
# # ● Fă același lucru cu un while.
print('---')
masina_preferata = 0
while masina_preferata < len(masini):
    # print(f'Masina mea preferata este {masina_preferata}')
    print(f'Masina mea preferata este {masini[masina_preferata]}')
    masina_preferata += 1
print('---')
# 2. Aceeași listă: Folosește un for else

masini_1 = []
index = 0
for cars_upper in masini:
    if index != 0 and index != len(masini)-1:
        masini_1.append(cars_upper.upper())
    else:
        masini_1.append(cars_upper)
    index += 1
else:
    print(masini_1)
print('---')
#
# # 3. Aceeași listă: Vine un cumpărător care dorește să cumpere un Mercedes.
# # Itereaza prin ea prin modalitatea aleasă de tine.
# # Dacă mașina e mercedes: Printează ‘am găsit mașina dorită de dvs’
# # Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# # Altfel: Printează ‘Am găsit mașina X. Mai căutam‘

for masina_dorita in masini:
    if masina_dorita == "Mercedes":
        print("am gasit masina dorita de dvs")
        break
    else:
        print("Am gasit masina X. Mai cautam")
print('---')
# 4. Aceași listă; Vine un cumpărător bogat dar indecis.
# # Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
# # - Dacă mașina e Trabant sau Lăstun: Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# # - Printează S-ar putea să vă placă mașina x
for bogat_indecis in masini:
    if bogat_indecis != "Trabant" or 'Lăstun':
        continue
print('S-ar putea sa va placa masina ' + random.choice(masini))
print('---')
# # # 5. Modernizează parcul de mașini:
# # Crează o listă goală, masini_vechi.
# # ● Itereaza prin mașini.
# # ● Când găsesti Lăstun sau Trabant:
# # - Salvează aceste mașini în masini_vechi.
# # - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# # ● Printează Modele vechi: x.
# # ● Modele noi: x.
#
# masini_vechi = []
# for masina in masini:
#     if masina == "Lăstun" or masina == "Trabant":
#         masini_vechi.append(masina)
#         modern = masini.index(masina)
#         masini[modern] = 'Tesla'
#         # masini_vechi.append(masina)
#         # masini = [masina.replace("Lăstun", "Trabant") for
#     # # print('Modele noi: ' )
# print(f'Modelele noi sunt: {masini}')
# print(f'Modelele vechi sunt: {masini_vechi}')
# print('---')
# # 6.Vine un client cu un buget de 15000 euro.
# # ● Prezintă doar mașinile care se încadrează în acest buget.
# # ● Itereaza prin dict.items() și accesează mașina și prețul.
# # ● Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
# # ● Iterează prin listă
#
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000}
#
# masini_buget = []
#  # pret_masini.values()
# for key, value in pret_masini.items():
#     if value < 15000:
#         print(f'pentru un buget sub 15000 euro, puteti alege masina {key}')
#         masini_buget.extend({key})
#         # print(masini_buget)
# # for pret_masini.values() in pret_masini:
# # print(pret_masini.values()
# for elem in masini_buget:
#     print("Masinile care se incadreaza in acest buget sunt: " + elem)
# print('---')
# # 7. Având lista:
# #     numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# # ● Iterează prin ea.
# # ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
#
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# print("---varianta 1---")
# lista_3 = []
# for value in numere:
#     if value == 3:
#         value +=1
#         lista_3.append(value)
#         print(f"am gasit 3 in lista de {len(lista_3)} ori")
#
# print("---varianta 2---")
# for value in numere:
#     while value == 3:
#         value += 1
#         print(f"am gasit 3 in lista")
#         break
# print('---')
# # 8. Aceeași listă:
# # ● Iterează prin ea
# # ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
#
# suma_n = 0
# for suma_numere in numere:
#     suma_n += suma_numere
#     print(suma_n)
# print('---')
#
# # 9. Aceeași listă:
# # ● Iterează prin ea.
# # ● Afișază cel mai mare număr (nu ai voie să folosești max).
#
# maxi = numere[0]
# for y in numere:
#     if y > maxi:
#         maxi = y
# print(maxi)
#
# print('---')
#
# # 10. Aceeași listă:
# # ● Iterează prin ea.
# # ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# # Ex: dacă e 3, să devină -3
# # ● Afișază noua listă.
#
# lista_negativa = [-neg for neg in numere]
# print(lista_negativa)
# print('---')
