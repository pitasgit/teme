# O variabila string este un sir de caractere de la tastatura delimitate de ‘‘
marca = 'Asus'
an_fabricatie = 2020
pret = 20.5
laptop_functional = True

print(type(marca))
print(type(an_fabricatie))
print(type(pret))
print(type(laptop_functional))

pret_round = (print(pret.__round__()))
print(type(pret_round))

print(f'Laptopul este marca {marca}.')
print(f'Este din anul {an_fabricatie}.')
print(f'Pretul a fost de {pret} Euro.')
print(f'Si numarul de bucati in stoc este {laptop_functional}.')

stoc = (int(laptop_functional))
print(f'Si numarul de bucati in stoc este {stoc}.')


numele = 'Ungureanu'
prenumele = 'Petre'

print(f'Numele complet are {len(numele + prenumele)} caractere')

lungimea = 7
latimea = 4

print(f'Aria dreptunghiului este {lungimea * latimea}')

string = 'Coral is either the stupidest animal or the smartest rock'
substring = string.count('the')
print(substring)

string = 'Coral is either the stupidest animal or the smartest rock'
substring = string.count('THE')
print(substring)

assert type(string) == type(int)

cuvant = 'sapte'
print(cuvant)
print(cuvant[2])

palindrom = 'madam'
if palindrom == palindrom[::-1]:
    print('acest string este palindrom')
else:
    print("acest string nu este palindrom")
