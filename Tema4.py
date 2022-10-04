# 1. Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# a)	Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’
# b)	Faceti acelasi lucru cu un for each
# c)	Faceti acelasi lucru cu un while

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range (0, len(masini)):
    print(f'Masina mea preferata este {masini[i]}')

for masina in masini:
    print(f'Maina mea preferata este {masina}')

i = 0
while i < len(masini):
  print(f'Maina mea preferata este {masini[i]}')
  i = i + 1

# 2.Aceeasi lista
# Folositi un for
# In for
#    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# Printati varianta finala a listei

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    masina = (masina[0].lower() + masina[1:-1].upper() + masina[-1].lower())
    print(masina)

# 3. Aceeasi lista,  Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin for each
# Daca masina e mercedes (if)
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam

for masina in masini:
    if masina == 'Mercedes':
        print('Am gasit masina dorita de dumneavoastra')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam')


# 4.Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x

for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

# 5. Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# -	Salvati aceste masini in masini_vechi
# -	Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x
masini_vechi = []
for masina in masini:
    if masina == 'Lastun ' or masina == 'Trabant':
        masini_vechi.append('Lastun')
        masini_vechi.append('Trabant')
print(masini_vechi)
masini[5] = 'Tesla'
masini[7] = 'Tesla'
print(masini)

# 6. Avand dict
pret_masini = {'Dacia': 6800, 'Lastun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000}

# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista
for marca, pret in pret_masini.items():
    if pret <= 15000:
        print(f'Pentru un buget de sub 15000 euro puteti alege masina {marca}')



# 7.Avand lista
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)


numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# 8.Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)

total = 0
for n in numere:
    total += n
print(total)

#9. Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)

x = numere[0]

for i in numere:
    if i>x:
        x=i
print(x)

# 10. Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

for i in numere:
    print(-abs(i))

# c. Optionale (may need google)
#
# 11.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for a in alte_numere:
    if a % 2 == 0:
       numere_pare.append(a)
print(numere_pare)
for b in alte_numere:
    if b % 2 == 1:
       numere_impare.append(b)
print(numere_impare)
for c in alte_numere:
    if c > 0 :
       numere_pozitive.append(c)
print(numere_pozitive)
for d in alte_numere:
    if d < 0 :
       numere_negative.append(d)
print(numere_negative)

# 13.Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# -	Nr secret e mai mare
# -	Nr secret e mai mic
# -	Felicitari! Ai ghicit!

import random
numar_secret = random.randint(1, 30)
numar_ghicit = None
while numar_ghicit != numar_secret:
    numar_ghicit = int(input('Ghiceste un numar intre 1 si 30'))
    if numar_secret > numar_ghicit:
        print(f'Nr secret e mai mare')
    elif numar_secret < numar_ghicit:
        print(f'Nr secret e mai mic')
    else:
        print(f'Felicitari! Ai ghicit')


# C05_EX01: Vrem sa salutam tara data ca argument pozitional si sa calculam suma a n numere date ca argumente
# optionale impreuna cu populatiile argumentelor keyword
def greet_and_sum_of_n_numers(country_name, *args, **kwargs):
    print(f'hello, {country_name}')

    return s
greet_and_sum_of_n_numers("Romania", 100, 11, 1, Romania=19_500_000, Moldova=4_000_000)
# ar trebui sa returneze: 23500111