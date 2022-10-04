# from datetime import date
# 1. Clasa Cerc
# Atribute: raza, culoare
# Constructor pt ambele atribute
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()
# import datetime
import math


class Cerc:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f'Raza cercului este {self.raza}')
        print(f'Culoarea cercului este {self.culoare}')

    def arie(self):
        return math.pi * (self.raza ** 2)

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return math.pi * self.diametru()


cerc1 = Cerc(3, 'rosu')
cerc2 = Cerc(5, 'alb')
cerc1.descriere_cerc()
print(f'Aria cercului 1 este {cerc1.arie()}')
print(f'Diametrul cercului 1 este {cerc1.diametru()}')
print(f'Circumferinta cercului 1 este {cerc1.circumferinta()}')
print('-----------------------')
print(f'Culoarea cercului 2 este {cerc2.culoare}')
print(f'Raza cercului 2 este {cerc2.raza}')
print(f'Aria cercului 2 este {cerc2.arie()}')
print(f'Diametrul cercului 2 este {cerc2.diametru()}')
print(f'Circumferinta cercului 2 este {cerc2.circumferinta()}')
print('-----------------------')


# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pt toate atributele
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
# Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi:

    def __init__(self, lungime, latime, culoare, culoare_noua):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
        self.culoare_noua = culoare_noua

    def descrie(self):
        print(f'Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}')

    def arie(self):
        return self.latime * self.lungime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoare(self, culoare_noua):
        print(f'Noua culoare este {culoare_noua}')


d1 = Dreptunghi(8, 5, 'verde', 'mov')
d2 = Dreptunghi(10, 4, 'albastru', 'gri')

print(f'Dreptunghiul 1 are lungimea {d1.lungime}, latimea de {d1.latime} si culoarea {d1.culoare}')
print(f'Dreptunghiul 1 are aria de {d1.arie()}')
print(f'Dreptunghiul 1 are perimetrul de {d1.perimetru()}')
print(f'Noua culoare va fi {d1.culoare_noua}')
print('-----------------------')
print(f'Dreptunghiul 2 are lungimea {d2.lungime}, latimea de {d2.latime} si culoarea {d2.culoare}')
print(f'Dreptunghiul 2 are aria de {d2.arie()}')
print(f'Dreptunghiul 2 are perimetrul de {d2.perimetru()}')
print(f'Noua culoare va fi {d2.culoare_noua}')
print('-----------------------')

# 3.Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)


class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        print(f'Nume: {self.nume}')
        print(f'Prenume: {self.prenume}')
        print(f'Salariu: {self.salariu}')

    def nume_complet(self):
        return self.nume + ' ' + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, marire):
        return (marire / self.salariu) * 100


a1 = Angajat('Popescu', 'Ion', 1000)
a1.descriere()
print(f'Numele complet al angajatului este {a1.nume_complet()}')
print(f'Salariul lunar al angajatului este {a1.salariu_lunar()}')
print(f'Salariul anual al angajatului este {a1.salariu_anual()}')
print(f'Salariul se va mari cu  {a1.marire_salariu(75)} %')
print('----------------')
a2 = Angajat('Ionescu', 'Maria', 1200)
a2.descriere()
print(f'Numele complet al angajatului este {a2.nume_complet()}')
print(f'Salariul lunar al angajatului este {a2.salariu_lunar()}')
print(f'Salariul anual al angajatului este {a2.salariu_anual()}')
print(f'Salariul se va mari cu  {a2.marire_salariu(80)} %')
print('---------------')


# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)


class Cont:
    def __init__(self, titular_cont, iban, sold):
        self.titular = titular_cont
        self.iban = iban
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular} are in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, suma):
        self.sold += suma
        print(f'{self.titular} a alimentat suma {suma} lei')
        print(f'{self.titular} are in cont {self.sold} lei')

    def creditare_cont(self, suma):
        if suma <= self.sold:
            self.sold -= suma
            print(f'{self.titular} a cheltuit suma de {suma}')
            print(f'{self.titular} mai are in cont {self.sold}')
        else:
            print('Fonduri insuficiente')

cont1 = Cont('Claudia Crivat', 'RO1', 300)
cont1.afisare_sold()
cont1.debitare_cont(500)
cont1.creditare_cont(100)

cont2 = Cont('Mihaela Popescu', 'RO2', 500)
cont2.afisare_sold()
cont2.debitare_cont(50)
cont2.creditare_cont(650)


# Optionale
# from tabulate import tabulate
class Factura:

    def __init__(self, serie, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume = nume_produs
        self.cantitate = cantitate
        self.pret = pret_buc
    def descriere(self):
        print(f'Factura cu {self.nume}, {self.numar}')
    def schimba_cantitatea(self, cantitate):
        print(f'Cantitatea este {self.cantitate}')
        self.cantitate += cantitate
        print(f'Cantitatea actualizata este {self.cantitate}')

    def schimba_pret(self, pret):
        print(f'Pretul este {self.pret}')
        self.pret += pret
        print(f'Pretul este {self.pret}')

    def schimba_nume(self, nume):
        self.nume = nume


# data = datetime.date
# print(f'Data: {date.today()}')
# p1 = Factura('abc', '000', 'Telefon', 7, 700)
# p1.schimba_cantitatea(5)
# p1.schimba_pret(100)
#
# p2 = Factura('abc', '001', 'Laptop', 5, 900)
# p2.schimba_cantitatea(6)
# p2.schimba_pret(150)



