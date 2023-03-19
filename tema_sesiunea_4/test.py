#  1.Având lista:
#
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
for masina_preferata in range(len(masini)):
        print(f'Masina mea preferata este {masini[masina_preferata]}')
print('---')
# ● Fă același lucru cu un for each.
for masina_preferata in masini:
    print(f'Masina mea preferata este {masina_preferata}')
# ● Fă același lucru cu un while.
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

# 3. Aceeași listă: Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes: Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel: Printează ‘Am găsit mașina X. Mai căutam‘

for masina_dorita in masini:
    if masina_dorita == "Mercedes":
        print("am gasit masina dorita de dvs")
        break
    else:
        print("Am gasit masina X. Mai cautam")
print('---')#
# 4. Aceași listă; Vine un cumpărător bogat dar indecis.
# Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun: Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# - Printează S-ar putea să vă placă mașina x
for bogat_indecis in masini:
    if bogat_indecis == "Trabant" or 'Lăstun':
        continue
print(f'S-ar putea sa va placa masina {masini}')
print('---')#