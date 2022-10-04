'''1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o.
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.'''

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

#2. De câte ori apare ‘do’?
print(note_muzicale.count('do'))

#3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
#Găsește 2 variante să le unești într-o singură listă

l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]

l3 = l1 + l2
print(l3)

l1.extend(l2)
print(l1)


'''4.● Sortează și afișează lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista'''
l3.sort()
print(l3)

'''5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
● Lista este goală.
● Lista nu este goală.'''

if len(l3) == 0:
    print('Lista  este goala')
else:
    print('Lista nu este goala')

#6. Folosește o funcție care să șteargă lista de la exercițiul 3
l3.clear()
print(l3)

#7. Copy paste la exercițiul 5. Verifică încă o dată.
#Acum ar trebui să se afișeze că lista e goală

if len(l3) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

#8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
#Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())


'''9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie'''

Ana = dict1['Ana']
Gigel = dict1['Gigel']
Dorel = dict1['Dorel']

print(f'Ana a luat nota {Ana}')
print(f'Gigel a luat nota {Gigel}')
print(f'Dorel a luat nota {Dorel}')


'''10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare'''

dict1.update({'Dorel': 6})
print(dict1)

'''11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi'''

dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

# TODO_2: Avand lista l=[1,1,2,3,1,4,4,5,6,2], cum facem sa
# eliminam duplicatele?
l=[1,1,2,3,1,4,4,5,6,2]
l = set(l)
print(l)

# C4_EX01: Print all even natural numbers lower than
# a keyboard inputed one. e.g.: in = 9 => 0 2 4 6 8

'''nr = int(input('Numar:'))
for nr in range (0, nr):
    if ( nr % 2 == 0):
        print(nr)'''

n = 15

while n>0:
    print(n)
    if(n% 5 == 0):
        n -= 2
    elif (n % 2 ==0):
        n -= 3
    else:
        n -= 1




