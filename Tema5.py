
# 1. Functie care sa calculeze si sa returneze suma a 2 numere
def sum(a, b):
    return a+b


s = sum(2, 5)
print(s)

# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def nr(a):
    if a % 2 == 0:
        return True
    else:
        return False
n = nr(5)
print(n)

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)


def nume(n1, n2):
    return len(n1+n2)
name = nume('Claudia','Crivat')
print(name)

# 4. Functie care returneaza aria dreptunghiului

def area(L, l):
    return L*l

a =area(3, 4)
print(a)

# 5. Functie care returneaza aria cercului
import math
def cerc(R):
    return (math.pi*R**2)
arie_cerc = cerc(5)
print(arie_cerc)

# 6. Functie care returneaza True daca un caracter x
# se gaseste intr-un string dat. Fasle daca nu

def caracter(word='bet'):
    if 'a' in word:
        return True
    else:
        return False
print(caracter())



# 7. Functie fara return, primeste un string si printeaza pe ecran:
# -	Nr de caractere lower case este x
# -	Nr de caractere upper case exte y


# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

def lst(numere):
    for i in numere:
        if i >= 0:
            return numere
numere = [4, 10, -5, 0, -2]
print(lst(numere))

# 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# -	Primul numar x este mai mare decat al doilea nr y
# -	Al doilea nr y este mai mare decat primul nr x
# -	Numerele sunt egale.

def nr(x, y):
    if x > y:
        print(f'Primul nr {x} este ai mare decat al doilea nr {y} ')
    elif y > x:
        print(f'Primul nr {y} este ai mare decat al doilea nr {x} ')
    else:
        print('Numerele sunt egale')
nr(6,10)
nr(12, 5)
nr(4, 4)

# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

def number(nr, set):
    if nr in set:
        set.add(nr)
        print('Am adaugat numarul nou in set')
        return True
    else:
        print('Nu am adaugat numarul in set. Acesta exista deja')
        return False
set = {1, 5, 8}
nr = 2
print(number(nr, set))



