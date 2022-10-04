#2Verifică și afișează dacă x este număr natural sau nu
x = int(input('Introduceti nr:'))
if x >= 0:
    print(f'Numarul {x} este numar natural')
else:
    print('Numarul introdus nu este numar natural')

#3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.


x = int(input('Introduceti nr:'))
if x > 0:
    print('Numarul este pozitiv')
elif x < 0:
    print('Numarul este negativ')
else:
    print('Numarul este neutru')

#4. Verifică și afișează dacă x este între -2 și 13

x = int(input('Introduceti nr.:'))
if x >= -2 and x <= 13:
    print(f'Numarul {x} se afla intre -2 si 13')
else:
    print('Numarul nu se afla in interval')

#5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

x = int(input('Introduceti X:'))
y = int(input('Introduceti Y:'))

if x >= y:
    diff = x - y
else:
    diff = y-x
if diff < 5:
    print('Diferenta este mai mica de 5')
else:
    print('Diferenta este mai mare de 5')

#v2
if abs(x-y) < 5:
    print('dif mai mare')
else:
    print('dif este mai mare sau egala')

#6.Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.

x = int(input('Introduceti nr:'))
i = range(5, 27)
if x not in i:
    print('Numarul nu este in intervalul (5,27)')
else:
    print('Numarul se afla in intervalul (5,27)')

#7.x și y (int)
#Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
x = input('Introduceti X:')
y = input('Introduceti Y:')
if x == y:
    print('Numerele sunt egale')
elif x>y:
    print(f'Numarul {x} este mai mare')
else:
    print(f'Numarul {y} este mai mare')


#8.X, y, z - laturile unui triunghi.
#Afișează dacă triunghiul este isoscel, echilateral sau oarecare

x = int(input('Latura1:'))
y = int(input('Latura2:'))
z = int(input('Latura3:'))
if x == y == z:
    print('Triunghiul este echilateral')
elif x == y or x == z or y == z:
    print('Triunghiul este isoscel')
else:
    print('Triunghiul este oarecare')

#9. Citește o literă de la tastatură.
#Verifică și afișează dacă este vocală sau nu.

l = input('Introduceti litera:')
l1 = l.lower()
vocale = 'aeiou'
if l1 in vocale:
    print(f'Litera {l1} este o vocala')
else:
    print(f'Litera {l1} este o consoana')


'''10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F'''

nota = int(input('Nota:'))
if nota >= 9:
    print('A')
elif nota >= 8:
    print('B')
elif nota >= 7:
    print('C')
elif nota >= 6:
    print('D')
elif nota >= 4:
    print('E')
elif nota <= 4:
    print('F')


#Exercitii optionale
#1.Verifică dacă x are minim 4 cifre (x e int).
#(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

x = int(input('Numar:'))
if len(str(x)) >= 4:
    print(f'Numarul are {len(str(x))} cifre')
else:
    print('Numarul nu are minim 4 cifre')

#2.Verifică dacă x are exact 6 cifre.

x = int(input('Numar:'))
if len(str(x)) == 6:
    print(f'Numarul are 6 cifre')
else:
    print('Numarul nu are 6 cifre')

#3.Verifică dacă x este număr par sau impar (x e int)

x = int(input('Numar:'))
if x % 2 == 0:
    print('Numarul este par')
else:
    print('Numarul este impar')

#4. x, y, z (int)
#Afișează care este cel mai mare dintre ele?

x = int(input('Introduceti x:'))
y = int(input('Introduceti y:'))
z = int(input('Introduceti z:'))
if x > y and x > z:
    print(f'Numarul {x} este cel mai mare')
elif y > x and y > z:
    print(f'Numarul {y} este cel mai mare')
else:
    print(f'Numarul {z} este cel mai mare')

#5. X, y, z - reprezintă unghiurile unui triunghi
#Verifică și afișează dacă triunghiul este valid sau nu



'''6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citește de la tastatură un int x
● Afișează stringul fără ultimele x caractere'''

str = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Numar'))
print(str[:-x])

#7. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5
str = 'Coral is either the stupidest animal or the smartest rock'
print(str[:6] + str[-5:])

'''#8. Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvânt
● output: 'Coral is either the stupidest animal or the smartest'''

str = 'Coral is either the stupidest animal or the smartest rock'
index = str.index('rock')
print(index)
print(str[0:index])

'''#11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
● Ai ghicit. Felicitări! Ai ales x si zarul a fost y.'''

x = int(input('Ghiceste numar:'))
import random
y = random.randint(1,6)
print(y)
if x < y:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {y}.')
elif x > y:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {y}.')
else:
    print(f'Ai ghicit. Felicitări! Ai ales {x} si zarul a fost {y}.')


