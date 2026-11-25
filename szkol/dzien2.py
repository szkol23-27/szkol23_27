# ============================================================
# 6. Lancuchy znakow (ciag dalszy)
# ============================================================

# Count

tekst = 'banana'

print(tekst.count("a"))  # 3 # liczenie malej litery a w tekscie
print(tekst.count("an")) # 2 # liczenie wystapienia 'an' w tekscie
print(tekst.count("x"))  # 0 # liczenie wystapienia 'x' w tekscie
print(tekst.count("A"))  # 0 # wielkosc liter ma znaczenie

zdanie = 'Dominik ma psa Lucjana a Lucjan ma dominika'
print(zdanie.count(" ma")) # 2 bierze pod uwage biale znaki, spacje


tekst = 'Ala ma kota'
print(tekst.count('a')) # 3 # liczenie malej litery a w tekscie
print(tekst.count('A')) # 1 # liczenie duzej litery A w tekscie

print(tekst.lower().count('a')) # 4 #liczenie wystapienia litery a bez wzgledu na wielkosc liter

tekst = 'aaaa'

print(tekst.count('aa')) # 2 # liczenie wystapienia 'aa', wystapienia nie moga na siebie nachodzic
print('aaa'.count('aa')) # 1 # po znalezieniu 'aa' szuka dalej za nim, zostaje samo 'a'

tekst = "  Hello world python"
print(tekst.count("  ")) # 1 # liczenie wystapienia podwojnej spacji '  '
print(tekst.count(' '))  # 4 # liczenie wystapienia spacji ' '

tekst = '2026-11-24'
print(tekst.count('-')) # 2 # liczenie wystapienia znaku '-'

# Strip
tekst = '   Hello world    '
print(1,tekst,1)            # 1    Hello world     1    # bez zmian
print(2,tekst.strip(),2)    # 2 Hello world 2           # lewa i prawa strona usuwanie bialych znakow (spacje, \n, \t)
print(3,tekst.lstrip(),3)   # 3 Hello world     3       # lewa strona usuwanie bialych znakow
print(4,tekst.rstrip(),4)   # 4    Hello world 4        # prawa strona usuwanie bialych znakow


#Usuwanie konkretnych znakow
print("****wow*****".strip("*"))   # wow # usuwanie znaku '*' z lewej i prawej strony
print("......wow.....".strip(".")) # wow # usuwanie znaku '.' z lewej i prawej strony

# pulapka: argument to ZESTAW znakow, nie tekst
print('abcba'.strip('ab'))         # c # usuwa kazde a i b z brzegow, w dowolnej kolejnosci


""" # przyklad uzycia
imie = input("podaj imie: ").strip()
print(imie)
"""

# split i join

# split
zdanie = 'Wygrana w totka wynosi 20 mln'
slowa = zdanie.split()
print(slowa)  # ['Wygrana', 'w', 'totka', 'wynosi', '20', 'mln'] # zamiana lancucha w liste

# split() bez argumentu dzieli po dowolnych bialych znakach (spacja, tab, \n) i skleja kilka pod rzad
# split(' ') dzieli po kazdej pojedynczej spacji
print('a  b'.split())      # ['a', 'b']
print('a  b'.split(' '))   # ['a', '', 'b'] podwojna spacja daje pusty element

# split po konkretnym
dane = 'Adam;25;Warszawa'
pola = dane.split(";") # ['Adam','25','Warszawa']
pola = dane.split()    # ['Adam;25;Warszawa']
print(pola)

#split z limitem
tekst = 'a-b-c-d-e'
print(tekst.split("-",2)) # ['a', 'b', 'c-d-e'] # dzieli tylko 2 pierwsze wystapienia, reszta jako jeden element

# join - laczy liste w string z separatorem
slowa = ['Ala','ma','kota']
print(" ".join(slowa))  # Ala ma kota   # laczenie w lancuch z listy z separatorem spacji
print("-".join(slowa))  # Ala-ma-kota   # laczenie w lancuch z listy z separatorem myslnika
print(", ".join(slowa)) # Ala, ma, kota # laczenie w lancuch z listy z separatorem ', '
print("".join(slowa))   # Alamakota     # laczenie w lancuch z listy bez separatora

# praktyczny przyklad
dane = ['Adam','25','Warszawa']
csv_line = ';'.join(dane)
print(csv_line) # Adam;25;Warszawa

# splitlines -- dzielenie po linijkach
tekst = 'linijka1\nlinijka2\nlinijka3'
print(tekst.splitlines()) # ['linijka1', 'linijka2', 'linijka3']
print(tekst.split('\n'))  # ['linijka1', 'linijka2', 'linijka3']

# roznica gdy tekst konczy sie na \n (tak konczy sie wiekszosc plikow)
tekst = 'linijka1\nlinijka2\n'
print(tekst.splitlines()) # ['linijka1', 'linijka2']
print(tekst.split('\n'))  # ['linijka1', 'linijka2', ''] pusty element na koncu


# 6.1 - Poproś użytkownika o imię i nazwisko (jedno input). Wyświetl: imię z wielkiej,
# nazwisko wielkimi literami. Np. "jan kowalski" → Jan KOWALSKI.

# Jak wyciagnac z listy konkretny potrzebny nam element? --> index dane[0],dane[1] etc.
# split()

""" pierwszy sposob
dane = input("Podaj imie i nazwisko: ")
imie, nazwisko = dane.split()
print(imie.capitalize(), nazwisko.upper())
"""

"""
dane = input("Podaj imię i nazwisko: ").split()
imie = dane[0].capitalize()
nazwisko = dane[1].upper()
print(imie, nazwisko)
"""

# 6.2 - Poproś o zdanie. Policz ile w nim jest liter a (zarówno a jak i A).
# count()

"""
sentence = input("Napisz jakieś zdanie: ")
print(sentence.lower().count('a'))
"""

"""
zdanie = input("Podaj zdanie: ")
liczba_a = zdanie.lower().count("a")
print("Liczba liter a i A:", liczba_a)
"""

# 6.3 - Poproś o tekst ze spacjami na początku i końcu. Oczyść go (strip), zamień na małe litery
# i wyświetl ile ma znaków.
#strip() len() lower()

"""
tekst = input("Podaj tekst ze spacjami na poczatku: ")
print(tekst.strip().lower())
print(len(tekst.strip().lower()))
"""

"""
tekst = input("Podaj tekst ze spacjami na początku i końcu: ")
tekst = tekst.strip().lower()
print("Tekst ma", len(tekst), "znaków.")
"""

# 6.6 - Mając string tekst = "Python jest super i Python jest prosty", zamień
# wszystkie Python na JavaScript i policz ile zamian zrobiono.
# count() replace()

"""
txt = "Python jest super i Python jest prosty"
print(txt.replace("Python","JavaScript"))
print('Liczba zmian:',txt.count('Python'))
"""

"""
tekst = "Python jest super i Python jest prosty"
liczba_zamian = tekst.count("Python")
nowy_tekst = tekst.replace("Python", "JavaScript")
print("Stary tekst:", tekst)
print("Nowy tekst:", nowy_tekst)
print("Liczba zrobionych zamian:", liczba_zamian)
"""


# – Łańcuchy funkcji

tekst = "    Witaj W PYTHONIE      "

# bez lancuchowania
wynik = tekst.strip()
wynik = wynik.lower()
wynik = wynik.replace("pythonie",'swiecie')
print(wynik) # witaj w swiecie


# za lancuchowaniem
wynik = tekst.strip().lower().replace('pythonie','swiecie')
print(wynik) # witaj w swiecie

# zla kolejnosc replace pulapka
wynik = tekst.strip().replace('pythonie','swiecie').lower()
print(wynik) # witaj w pythonie


# praktyczny przyklad
email = '   Adam.Kowalski@MAIL.COM   '
czysty = email.strip().lower()
print(czysty) # adam.kowalski@mail.com

# lancuchowanie split + join
tekst  = ' za   duzo   spacji  '
czysty = " ".join(tekst.split())
print(1,czysty,1) # 1 za duzo spacji 1


# – Iterowanie po łańcuchach tekstowych

tekst = "Python"

# Tekst:   P y t h o n
# Indeks:  0 1 2 3 4 5


# indeksy
# dostep do konkretnej litery w lancuchu
print(tekst[0])     # P
print(tekst[5])     # n
# print(tekst[10])  # IndexError: string index out of range
print(tekst[-1])    # n
print(tekst[-3])    # h
# print(tekst[-10])   # IndexError: string index out of range


for litera in tekst:
    print(litera)

# Wynik
# P
# y
# t
# h
# o
# n

# enumerate - dodatkowo numeracja uzyteczna w petlach

for index,litera in enumerate(tekst):
    print(f'Indeks: {index}: "{litera}"')

print('*'*20)
for index,litera in enumerate("ABC",start=1):
    print(f'Indeks: {index}: "{litera}"')

# Metody sprawdzajace znaki

# .isalpha()       - czy same litery
# .isdigit()       - czy same cyfry
# .isalnum()       - czy litery i/lub cyfry
# .isspace()       - czy same białe znaki
# .islower()       - czy wszystkie litery małe
# .isupper()       - czy wszystkie litery wielkie
# .istitle()       - czy każde słowo z wielkiej
# .isnumeric()     - czy same znaki numeryczne
# .isidentifier()  - czy poprawna nazwa zmiennej
# .startswith(x)   - czy zaczyna się od x
# .endswith(x)     - czy kończy się na x


# – Mnożenie tekstu. Ale jak?
print('Ha'*30)  # HaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHa
print('-'*40)   # ----------------------------------------
print('='*40)   # ========================================
print('*'*40)   # ****************************************

# praktyczne zastosowanie - formatowanie
#  wysrodkowanie tekstu w konkretnej ilosci znakow
tytul = 'Raport'
print('=' * 30)             # ==============================
print(f'{tytul:^30}')       #            Raport           
print('=' * 30)             # ==============================

# Wygodne sprawdzanie czy tekst zawiera frazę

tekst = 'Start szkolenia z Javy zaczyna sie tego i tego'

# in - czy zawiera fraze?
print('Javy' in tekst)           # True
print('javy' in tekst)           # False
print('pythona' in tekst)        # False
print('javy' in tekst.lower())   # True

# not in
if 'python' not in tekst.lower():
    print('Brak pythona!')

# startswith
print(tekst.startswith('Start'))            # True --> zaczyna sie od 'Start'
print(tekst.lower().startswith('start'))    # True --> po lower() tekst zaczyna sie od 'start', wielkosc liter bez znaczenia
print(tekst.startswith('Programowanie'))    # False --> nie zaczyna sie

# endswith
plik = 'zdjecie.png'
print(tekst.endswith('tego')) # True
print(plik.endswith('.png'))  # True
print(plik.endswith('.jpg'))  # False
print(plik.endswith(('.jpg','.png','.gif')))  # True # krotka


# find --> szuka wystapienia i zwraca nam indeks

print(tekst.find("Javy"))    # 18 # zwraca indeks pierwszego wystapienia szukanej frazy
print(tekst.find("python"))  # -1 # brak frazy, uwaga: -1 to tez poprawny indeks (ostatni znak), sprawdzaj != -1

# index --> czyli w stylu find, ale wyrzuci nam blad jak nie znajdzie szukanej frazy

print(tekst.index("Javy"))   # 18
# print(tekst.index("python")) ValueError: substring not found


# Czy Python > Java --> porownywanie

# Przy str mozemy korzystac z operatorow porownania == != < > <= >=

print("Python" == "Python") # True
print("python" == "Python") # False

# porownywanie < > <= >= idzie znak po znaku po kodach Unicode (ord)
print("Python" > "Java")  # True  P (80) > J (74)
print("apple" < 'banana') # True  a (97) < b (98)
print("abc" < "abd")      # True  porownuje znak po znaku 99 < 100
print("abc" >= "abd")     # False

# pulapki
print('Zebra' < 'apple')  # True  Z (90) < a (97), wielkie litery sa "mniejsze" od malych
print('ząb' < 'zebra')    # False ą (261) > e (101), polskie znaki sa daleko w tabeli


print(ord('P')) # 80
print(ord('J')) # 74
print(ord('a')) # 97
print(ord('b')) # 98
print(ord('c')) # 99
print(ord('d')) # 100

print(chr(80)) # P

# – Cięcia, cięcia - o cięciu łańcuchów tekstowych słów kilka

tekst = 'Programowanie'

# [start:stop:step]
# stop NIE wchodzi do wyniku (jest wylaczny)
# chcesz miec element o indeksie 10 wlacznie, wpisz stop = 11
# tekst[0:4] daje Prog, czyli indeksy 0,1,2,3 (4 juz nie)

# podstawowe slice
print(tekst[0])     # P
print(tekst[-1])    # e
print(tekst[0:4])   # Prog
print(tekst[0:])    # Programowanie
print(tekst[:4])    # Prog

# z krokiem
print(tekst[::2])       # Pormwne
print(tekst[::-1])      # einawomargorP
print(tekst[1:6:-1])    #
print(tekst[6:0:-1])    # margor

# omijanie bledu
# print(tekst[100])      # IndexError: string index out of range
print(tekst[100:101])    # brak bledu typowego dla indexowania poza obszar

# palindrom ---> odwrocone slowo jest takie samo jak oryginal
slowo = "kajak"
print(slowo == slowo[::-1]) # True


# f-string formatowanie tekstu

imie = 'adam'
wiek = 25

# podstawowe
print(f'{imie} ma {wiek} lat')          # adam ma 25 lat
print(f'{imie:<20}')                    # adam                
print(f'{imie:>20}')                    #                 adam
print(f'{imie:^20}')                    #         adam        
print(f'{imie:*^20}')                   # ********adam********

# formatowanie liczb
pi = 3.14159265358979
print(f'{pi:.2f}')          # 3.14 dwa miejsca po przecinku
print(f'{pi:.3f}')          # 3.142 zaokragla, nie ucina
print(f'{1000000:,}')       # 1,000,000 separator tysiecy
print(f'{0.85:.0%}')        # 85%


# 6.7 - Poproś o PESEL (11 cyfr). Wytnij (slicing) i wyświetl: rok urodzenia, miesiąc, dzień.
# uwaga: nie bierzemy pod uwage osob urodzonych po 2000 roku (tam miesiac w PESEL jest powiekszony o 20)

"""
pesel = input('Podaj pesel: ')
year = int(pesel[0:2])
month = int(pesel[2:4])
day = int(pesel[4:6])
print(f'Rok: 19{year}')
print(f'Miesiac: {month}')
print(f'Dzien: {day}')
"""

# 6.8* - Napisz program sprawdzający czy podane słowo jest palindromem (czytane od przodu i tyłu tak samo, np. kajak, anna). Ignoruj wielkość liter.
"""
slowo = input("Podaj słowo: ").lower()
if slowo == slowo[::-1]:
    print("Palindrom!")
else:
    print("Nie palindrom.")
"""

# ============================================================
# 7. Listy
# ============================================================

# – Tworzenie list

# pusta lista
pusta  = []
pusta2 = list()

# range(start, stop), stop wylaczny, chcesz do 11 wlacznie, wpisz 12
lista_od_1_do_11 = range(1,12)
print(lista_od_1_do_11)         # range(1, 12) range to osobny obiekt, nie lista
print(list(lista_od_1_do_11))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# lista liczb, napisow, bool, floatow, mieszane
liczby = [2,4,5,3,4,5,6]
napisy = ['adam','rafal','ala','dominik']
prawda = [True, False, True, False]
zmiennoprze = [56.3,23.4,34.6,28.5]
mieszana = [True, 45.7, 'adam','rafal', 3]


# Pobieranie wartości z list

owoce = ["jabłko", "banan", "gruszka", "kiwi", "mango"]

# owoce   jablko banan gruszka kiwi mango
# index      0     1      2      3    4

# wyciaganie jednego elementu
print(owoce[0])  # jablko
print(owoce[-1]) # mango
print(owoce[3])  # kiwi
# print(owoce[10]) # IndexError: list index out of range

# wycinanie (slicing) ciecie -fragment listy
print(owoce[:])     # cala lista ['jabłko', 'banan', 'gruszka', 'kiwi', 'mango']
print(owoce[2:])    # od indeksu 2 do konca ['gruszka', 'kiwi', 'mango']
print(owoce[:4])    # od poczatku do indeksu 3 wlacznie ['jabłko', 'banan', 'gruszka', 'kiwi']
print(owoce[2:4])   # od indeksu 2 do indeksu 3 wlacznie ['gruszka', 'kiwi']
print(owoce[::2])   # co drugi element ['jabłko', 'gruszka', 'mango']

#pulapka z indeksowaniem - ominiecie bledu IndexError
print(owoce[10:11]) # [] zamiast bledu pusta lista

#wycinanie z ujemnym krokiem
print(owoce[::-1])     # odwrocona lista cala
print(owoce[::-2])     # odwrocona lista co 2 element
print(owoce[0:3:-1])   # [] pulapka, przy kroku ujemnym start musi byc wiekszy od stop
print(owoce[3:0:-1])   # ['kiwi', 'gruszka', 'banan'] stop 0 wylaczny, jablka brak
print(owoce[-2:0:-1])  # ['kiwi', 'gruszka', 'banan'] bez mango, ale tez bez jablka
print(owoce[-2::-1])   # ['kiwi', 'gruszka', 'banan', 'jabłko'] bez mango, jablko jest

# Iterowanie po listach

owoce = ["agrest", "marakuja", "avocado"]

for owoc in owoce:
    print(owoc)

for index,owoc in enumerate(owoce,start=1):
    print(f'{index}-{owoc}')

# – Sprawdzanie czy element znajduje się na liście
# operator in sprawdza czy element jest naliscie
owoce = ['malina','wisnia','porzeczka']

print('banan' in owoce)         # False
print('wisnia' in owoce)        # True
print('wisnia' not in owoce)    # False

if 'wisnia' in owoce:
    print('Na liscie zakupowej znajduje sie wisnia')
print('*'*30)

# Modyfikowanie zawartości listy

# – Dodawanie nowych wartości i wstawianie w miejsce istniejących

imiona = ['ala','damian','agnieszka','rafal']
print(imiona)   # ['ala', 'damian', 'agnieszka', 'rafal']

# zmiana jednego elementu
imiona[1] = 'dominik'
print(imiona)   # ['ala', 'dominik', 'agnieszka', 'rafal']

#zmiana kilku elementow naraz (slicing)
# imiona[1:3] = 'sakrament' # pulapka - nie opakowany element w liste dodaje sie kazdy znak oddzielnie jako element
# print(imiona)

imiona[1:3] = ['Kordian','Wokulski']
print(imiona)   # ['ala', 'Kordian', 'Wokulski', 'rafal']

# dodawanie nowych wartosci append(), insert(), extend()

auto = ['ford','toyota']
print(auto)      # ['ford', 'toyota']

# append() - dodaje na sam koniec listy
auto.append('BMW')
print(auto)      # ['ford', 'toyota', 'BMW']

"""
# zagniezdzenie listy przy append 1 element
auto.append(['BMW','Tesla'])
print(auto)
print(auto[3])
print(auto[3][0])
"""

# blad append za duzo argumentow
# auto.append('BMW','Tesla') # TypeError: list.append() takes exactly one argument (2 given)

# insert() - wstaw na dowolny konkretny indeks
auto.insert(1,'tesla')  # ustawia na pierwszy indeks dany element
auto.insert(10,'tesla') # nie wywali bledu, przeniesie na ostatni mozliwy index
print(auto)     # ['ford', 'tesla', 'toyota', 'BMW', 'tesla']

# extend() - dodaje wiele elementow do listy z innej listy
auto.extend(['honda','mitsubishi'])
print(auto)         # ['ford', 'tesla', 'toyota', 'BMW', 'tesla', 'honda', 'mitsubishi']

# pulapki extend
# auto.extend('honda','mitsubishi') TypeError: list.extend() takes exactly one argument (2 given)
# auto.extend('honda') # doda --> 'h', 'o', 'n', 'd', 'a
# print(auto)

# dodawanie dwoch list w inny sposb
nowa = ['jablko','gruszka'] + ['agrest']
print(nowa)         # ['jablko', 'gruszka', 'agrest']

# 7.22A - Lista zakupów. Stwórz pustą listę zakupy, a potem:

# a) za pomocą append() dodaj kolejno "chleb", "mleko" i
# "masło", wyświetl listę,
# b) wstaw "jajka" na sam początek, a "ser" tuż przed
# ostatni element (użyj indeksu ujemnego) i wyświetl listę.
# Oczekiwany wynik: ['jajka', 'chleb', 'mleko', 'ser', 'masło'].

zakupy = []
zakupy.append('chleb')
zakupy.append('mleko')
zakupy.append('maslo')
print(zakupy)               # ['chleb', 'mleko', 'maslo']
zakupy.insert(0,'jajka')
zakupy.insert(-1,'ser')
print(zakupy)               # ['jajka', 'chleb', 'mleko', 'ser', 'maslo']

# 7.28A - Kolejka do lekarza. Zacznij od
# kolejka = ["Adam", "Ola"] i po kolei:

#  a) przychodzą "Kasia" i "Tomek" - dodaj ich na koniec,
#  b) pilny pacjent "Zofia" wchodzi na sam początek,
#  c) przyjeżdża grupa ["Bartek", "Ewa", "Jan"] -
#  dodaj wszystkich na koniec jedną operacją tak,
#  żeby lista została płaska (sprawdź len()),
#  d) "Marek" ma umówioną wizytę i ma być trzeci w kolejce,
#  e) wypisz kolejkę w formacie 1. Zofia, 2. Adam, ... oraz
#  liczbę czekających osób (powinno być 9).

""" rozwiazanie 1
kolejka = ["Adam", "Ola"]
kolejka.append('Kasia')
kolejka.append('Tomek')
kolejka.insert(0,'Zofia')
grupa = ["Bartek", "Ewa", "Jan"]
for idx in range(len(grupa)):
    kolejka.append(grupa[idx])
kolejka.insert(2,'Marek')

for idx in range(len(kolejka)):
    print(f'{idx+1} {kolejka[idx]}')
print(f'Liczba osób oczekujących: {len(kolejka)}')
"""

""" rozwiazanie 2
kolejka = ["Adam", "Ola"]
kolejka.extend(["Kasia", "Tomek"])
print(kolejka)
kolejka.insert(0,"Zofia")
print(kolejka)
kolejka.extend(["Bartek", "Ewa", "Jan"])
print("Długość po dodaniu grupy:", len(kolejka))
print(kolejka)
kolejka.insert(2,"Marek")
print(kolejka)
sformatowana_kolejka = [f"{i}. {osoba}" for i, osoba in enumerate(kolejka, start=1)]
print(", ".join(sformatowana_kolejka))
print("Liczba czekających osób:", len(kolejka))
"""


# Kasowanie elementów z listy

# remove() pop() del clear()

miasta = ['Warszawa','Krakow','Poznan','Berlin','Bedzin','Lodz','Gdynia','Berlin']
print(miasta) # ['Warszawa', 'Krakow', 'Poznan', 'Berlin', 'Bedzin', 'Lodz', 'Gdynia', 'Berlin']

# remove - usuwa pierwsze wystapienie wartosci
miasta.remove('Berlin')
print(miasta) # ['Warszawa', 'Krakow', 'Poznan', 'Bedzin', 'Lodz', 'Gdynia', 'Berlin']

# miasta.remove('Paris') # ValueError: list.remove(x): x not in list

# pop() - bez indexu - usuwa ostatni i zwraca usuniety element
usuniety_ostatnia = miasta.pop()
print(usuniety_ostatnia)    # Berlin
print(miasta)               # ['Warszawa', 'Krakow', 'Poznan', 'Bedzin', 'Lodz', 'Gdynia']

# pop() usuwa po indexie i zwraca usuniety element
# usuniety = miasta.pop(34) # IndexError: pop index out of range
usuniety = miasta.pop(3)
print(usuniety)             # Bedzin
print(miasta)               # ['Warszawa', 'Krakow', 'Poznan', 'Lodz', 'Gdynia']

# del - usuwa po indexie (nie zwraca)

del miasta[0]
# del miasta[9]      # IndexError: list assignment index out of range
print(miasta)        # ['Krakow', 'Poznan', 'Lodz', 'Gdynia']


# clear() - czysci liste do zera
miasta.clear()
print(miasta)   # []

# 7.23 - Porządki na liście. Na liście zwierzeta = ["pies", "kot", "chomik", "kot", "papuga", "rybka"]
# wykonaj po kolei i po każdym kroku wyświetl listę:

#     a) usuń pierwszego "kot" (remove),
#     b) usuń pierwszy element (del),
#     c) zdejmij ostatni element i wyświetl, co usunąłeś (pop),
#     d) zdejmij element o indeksie 1 i wyświetl, co usunąłeś (pop),
#     e) usuń "słoń", ale tylko jeśli jest na liście - inaczej wyświetl Nie ma słonia,
#     f) wyczyść listę (clear).


zwierzeta = ["pies", "kot", "chomik", "kot", "papuga", "rybka"]
# a) usuń pierwszego "kot"
zwierzeta.remove("kot")
print(zwierzeta)
# b) usuń pierwszy element
del zwierzeta[0]
print(zwierzeta)
# c) zdejmij ostatni element i wyświetl, co usunąłeś
usuniete = zwierzeta.pop()
print("Usunięto:", usuniete)
print(zwierzeta)
# d) zdejmij element o indeksie 1 i wyświetl, co usunąłeś
usuniete = zwierzeta.pop(1)
print("Usunięto:", usuniete)
print(zwierzeta)
# e) usuń "słoń", ale tylko jeśli jest na liście
if "słoń" in zwierzeta:
    zwierzeta.remove("słoń")
else:
    print("Nie ma słonia")
print(zwierzeta)
# f) wyczyść listę
zwierzeta.clear()
print(zwierzeta)


# Funkcje wbudowane w listy
# – Sortowanie i odwracanie list
# .sort() sorted()
liczby = [4,2,8,1,5]
print(liczby)       # [4,2,8,1,5]

#sort() - sortuje w miejscu (zmienia on oryginalna liste)
liczby.sort()
print(liczby)        # [1, 2, 4, 5, 8]

# sort malejaca
liczby.sort(reverse=True)
print(liczby)       # [8, 5, 4, 2, 1]


# sorted() - zwraca nam nowa liste, oryginal bez zmian
oryg = [4,2,8,1,5]
nowa = sorted(oryg)
print(sorted(oryg))                     # [1, 2, 4, 5, 8]
print(oryg)                           # [4,2,8,1,5]
print(nowa)                          # [1, 2, 4, 5, 8]
print(sorted(oryg,reverse=True))    # [8, 5, 4, 2, 1]


owoce = ["jabłko", "banan", "gruszka"]
owoce.sort()
print(owoce)

owoce.reverse()
print(owoce)


# – Inne ciekawe funkcje i możliwości

liczby = [4, 2, 8, 1, 5, 3, 7, 6]
print(len(liczby)) # 8  - dlugosc listy
print(min(liczby)) # 1  - minimalna wartosc listy
print(max(liczby)) # 8  - maksymalna wartosc
print(sum(liczby)) # 36 - suma wszystkich elementow

# count()
oceny = [5,2,5,2,4,5,3,5,2,5]
print(oceny.count(5)) # 5 - ilosc wystapien
print(oceny.index(3)) # 6


# pulapka miszana lista, albo str
liczby = [True, 2, 'str', 1, 'Adam', 3, 7, 6]
print(len(liczby)) # 8  - dlugosc listy
# print(min(liczby)) # TypeError: '<' not supported between instances of 'str' and 'bool'
# print(max(liczby)) # TypeError: '>' not supported between instances of 'str' and 'int'
# print(sum(liczby))   # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# str wbudowane
str_lista = ['banan','apple','str']
print(len(str_lista)) # 3  - dlugosc listy (ilosc elementow, nie liter)
print(min(str_lista)) # apple  - minimalna wartosc listy
print(max(str_lista)) # str  - maksymalna wartosc
# print(sum(str_lista)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'


# kopiowanie listy = uwaga na pulapke
a = [1,2,3]
b = a
b.append(4)
print(a) # [1, 2, 3, 4] - a tez sie zmienia

# dobrze - kopia listy
a = [1,2,3]
b = a.copy()   # sposob 1
b = a[:]       # sposob 2
b = list(a)    # sposob 3
b.append(4)
print(a)       # [1, 2, 3] oryginal bez zmian

# rozpakowanie listy
owoce = ['jablko', 'banan', 'gruszka']
pierwszy, drugi, trzeci = owoce
print(pierwszy,drugi,trzeci) # jablko banan gruszka

# rozpakowywanie reszty *
liczby = [1,4,5,6,7,3]
pierwszy, *reszta = liczby
print(reszta)   # [4, 5, 6, 7, 3]
print(pierwszy) # 1

# zip()

imiona = ['Adam', 'Ola', 'Kasia']
wiek = [20,43,25]

polaczenie = zip(imiona,wiek)
print(polaczenie)        # <zip object at 0x70e6ddfe53c0>
print(list(polaczenie))  # [('Adam', 20), ('Ola', 43), ('Kasia', 25)]

for imie, w in zip(imiona,wiek):
    print(f'{imie} ma {w} lat')

print('*'* 30)
# zachowanie zip dla niewymiarowych list
# zip konczy na najkrotszej liscie, nadmiar jest pomijany po cichu (bez bledu)
imiona = ['Adam', 'Ola', 'Kasia','Dominik','Rafal']
wiek = [20,43,25]

for imie, w in zip(imiona,wiek):
    print(f'{imie} ma {w} lat')

# Adam ma 20 lat
# Ola ma 43 lat
# Kasia ma 25 lat
# Dominik i Rafal pominieci


# ============================================================
# 8. Krotki
# ============================================================
# uporzadkowana sekwencja elementow, jak lista, ale niezmienna
# mozna miec duplikaty, dostep po indeksie, nie mozna dodawac, usuwac ani podmieniac elementow

pusta  = ()
pusta2 = tuple()
print(pusta)  # ()
print(pusta2) # ()

# krotka z elementami
owoce = ('jablko','banan','gruszka')
liczby = (2,5,6,4,3)

# krotka mieszana
mix_masz = ('maksimjum', 4, 4.65, True)

# krotka bez nawiasow
kolory = 'czerwony','zielony','niebieski'
print(type(kolory))         # <class 'tuple'>
print(kolory)               # ('czerwony', 'zielony', 'niebieski')
krotka_jedna = 'ha',
print(type(krotka_jedna))   # <class 'tuple'>


# uwaga pulapka
nie_krotka = ('jablko')
krotka = ("jablko",)
print(type(nie_krotka)) # <class 'str'>
print(type(krotka))     # <class 'tuple'>


# konwersja
lista = [1,2,3]
krotka = tuple(lista)
z_powrotem = list(krotka)
print(lista,krotka,z_powrotem) # [1, 2, 3] (1, 2, 3) [1, 2, 3]

# Uzupelnianie krotek danymi

owoce = ('jablko','banan')

#laczenie krotek operatorem +
# owoce = owoce + ('gruszka') # TypeError: can only concatenate tuple (not "str") to tuple
owoce = owoce + ('gruszka',)
print(owoce) # ('jablko', 'banan', 'gruszka')

# mnozenie krotek
powtorzona = ('ha',) * 3
print(powtorzona) # ('ha', 'ha', 'ha')


# hahaha = "ha", * 3 TypeError: Value after * must be an iterable, not int

# # dodawanie za pomoca konwersje
# owoce = ('jablko','banan')
# temp = list(owoce)
# temp.append("kiwi")
# temp.insert(1,"mango")
# owoce = tuple(temp)
# print(owoce) # ('jablko', 'mango', 'banan', 'kiwi')


# Pobieranie wartosci z krotki

owoce = ("jabłko", "banan", "gruszka", "kiwi", "mango")

# indexowanie
print(owoce[0])    # jablko
print(owoce[3])    # kiwi
# print(owoce[50]) # IndexError: tuple index out of range
print(owoce[-1])   # mango

# slicing
print(owoce[1:3])  # ('banan', 'gruszka')
print(owoce[:3])   # ('jabłko', 'banan', 'gruszka')
print(owoce[2:])   # ('gruszka', 'kiwi', 'mango')
print(owoce[::2])  # ('jabłko', 'gruszka', 'mango')


# Rozpakowywanie krotek

punkt = (10, 20)
x ,y = punkt
print(f'x={x}:y={y}') # x=10:y=20

dane = ('adam', 25, 'Polska', 'Warszawa')
imie, wiek, *reszta = dane
print(imie,wiek,reszta)  # adam 25 ['Polska', 'Warszawa']

# zamiana wartosci zmiennych

a = 5
b = 10
a , b = b , a
print(a,b) # 10 5

# Funkcje
owoce = ("jabłko", "banan", "gruszka")
print(owoce.count("banan"))             # 1
print(owoce.index("gruszka"))           # 2
print("jabłko" in owoce)                # True
# dziala len, min, max, sum

# Pulapka sorted() na krotce, sorted zwraca NOWA LISTE, krotka zostaje bez zmian
liczby = (2,5,4,6,3,6)
print(sorted(liczby))        # [2, 3, 4, 5, 6, 6] wynik to lista, nie krotka
print(tuple(sorted(liczby))) # (2, 3, 4, 5, 6, 6) chcesz krotke, opakuj w tuple()
print(liczby)                # (2, 5, 4, 6, 3, 6) oryginal bez zmian
# liczby.sort()  # AttributeError: 'tuple' object has no attribute 'sort'

# 8.1 - Stwórz krotkę z 4 porami roku. Wyświetl pierwszą i ostatnią.

pory_roku = ('Wiosna', 'Lato', 'Jesien', 'Zima')
print(f'Pierwsza: {pory_roku[0]}, ostatnia: {pory_roku[-1]}') # Pierwsza: Wiosna, ostatnia: Zima

# 8.5 - Stwórz dwie zmienne a = 100 i b = 200. Zamień ich
# wartości za pomocą krotki (bez trzeciej zmiennej).

a=100
b=200
a, b = b, a
print("a-", a,",b-",b) # a- 200 ,b- 100

# 8.7 - Mając krotkę owoce = ("jabłko", "banan", "gruszka"),
# dodaj do niej "kiwi" i "mango" (tworząc nową krotkę).

owoce = ("jabłko", "banan", "gruszka")
nowa = owoce + ("kiwi", "mango")
print(nowa) # ('jabłko', 'banan', 'gruszka', 'kiwi', 'mango')

# ============================================================
# 9. Słowniki
# ============================================================
# kolekcja par klucz:wartosc

# pusty slownik
pusty = {}
pusty2 = dict()
print(pusty,pusty2) # {} {}

# slownik z danymi
# "imie" i "Imie" to dwa rozne klucze, wielkosc liter ma znaczenie
osoba = {
    "imie": "Adam",
    "wiek": 25,
    "miasto":"Warszawa",
    "Imie": "Rafal",
    "bezrobotny": False
}
print(osoba)   #  {'imie': 'Adam', 'wiek': 25, 'miasto': 'Warszawa', 'Imie': 'Rafal', 'bezrobotny': False}

osoba2 = dict(imie='Damian',wiek=27,miasto='Lodz')
print(osoba2) # {'imie': 'Damian', 'wiek': 27, 'miasto': 'Lodz'}

wiek = [25,37,23]
imie = ['damian','kamil','rafal']

polaczone = list(zip(imie,wiek))
print(polaczone)        # [('damian', 25), ('kamil', 37), ('rafal', 23)]
slownik = dict(polaczone)
print(slownik)          # {'damian': 25, 'kamil': 37, 'rafal': 23}
# pierwsza lista w zip to klucze, druga to wartosci
# klucze musza byc unikalne, powtorzony klucz nadpisuje poprzednia wartosc

# zagniezdzenia
firma = {
    "nazwa": "Techcorp",
    "adres": {
        "ulica": 'Marszalkowska',
        "miasto": 'Krakow'
    },
    "pracownicy": ['Adam','Rafal','Damian']
}


print(firma['adres']["miasto"])  # Krakow
print(firma['pracownicy'][0])    # Adam


# Pobieranie wartosci ze slownikow

zwierzak = {'rasa':'piesowaty',"wiek":25,'badanie':True,'chip':False}

# przez nawias [] - wyrzuci blad jesli klucz nie istnieje
print(zwierzak['rasa'])   # piesowaty
print(zwierzak['wiek'])   # 25
# print(zwierzak['email'])  # KeyError: 'email'

# przez .get() - bezpieczne, zwraca None lub domyslna wartosc
print(zwierzak.get('rasa'))              # piesowaty
print(zwierzak.get('email'))             # None
print(zwierzak.get('email','brak'))      # brak


# Iterowanie po slowniku
osoba = {"imie": "Adam", "wiek": 25, "miasto": "Warszawa"}

# po kluczach (domyslnie)
for klucz in osoba:
    print(klucz)

# po kluczach niedomyslne
for klucz in osoba.keys():
    print(klucz)

# imie
# wiek
# miasto

# po wartosciach
for wartosc in osoba.values():
    print(wartosc)

# Adam
# 25
# Warszawa

for klucz,wartosc in osoba.items():
    print(f'Klucz:{klucz}-wartosc:{wartosc}')

# Klucz:imie-wartosc:Adam
# Klucz:wiek-wartosc:25
# Klucz:miasto-wartosc:Warszawa


# Sprawdzanie czy klucz istnieje

osoba = {"imie": "Damian","wiek":50}

print("imie" in osoba)              # True
print("email" in osoba)             # False
print('email' not in osoba)         # True

if "wiek" in osoba:
    print(f'Wiek: {osoba['wiek']}') # print("imie" in osoba)


# Zamiana na listy/krotki

osoba = {"imie": "Adam", "wiek": 25, "miasto": "Warszawa"}

print(len(osoba))             # 3
print(list(osoba))            # ['imie', 'wiek', 'miasto']
print(list(osoba.keys()))     # ['imie', 'wiek', 'miasto']
print(list(osoba.values()))   # ['Adam', 25, 'Warszawa']
print(list(osoba.items()))    # [('imie', 'Adam'), ('wiek', 25), ('miasto', 'Warszawa')]

# Modyfikacja zawartosci slownikow

osoba = {"imie": "Adam", "wiek": 25}
print(osoba) # {'imie': 'Adam', 'wiek': 25}

# dodawanie i podmiana
osoba['imie'] = 'Ala' # podmienianie wartosci w slowniku jesli klucz istnieje
osoba['miasto'] = 'Krakow' # dodanie nowych wartosci klucz:wartosc jak klucz nie istnieje
print(osoba)  # {'imie': 'Ala', 'wiek': 25, 'miasto': 'Krakow'}

# update - dodaje/aktualizuje wiele par naraz
osoba.update({"email":'adam@gmail.com',"wiek":39}) # dodanie nowego klucza oraz edycja jednego
print(osoba) # {'imie': 'Ala', 'wiek': 39, 'miasto': 'Krakow', 'email': 'adam@gmail.com'}

# setdefault - dodaje klucz tylko jesli jeszcze nie istnieje
osoba.setdefault('miasto','Warszawa') # klucz istnieje pomija
print(osoba)  # {'imie': 'Ala', 'wiek': 39, 'miasto': 'Krakow', 'email': 'adam@gmail.com'}
osoba.setdefault('status','szczepiony') # klucz nie isntieje --> nowa wartosc
print(osoba) # {'imie': 'Ala', 'wiek': 39, 'miasto': 'Krakow', 'email': 'adam@gmail.com', 'status': 'szczepiony'}

# Usuwanie elementow

# del - usuwa po kluczu
del osoba['status']
print(osoba) # {'imie': 'Ala', 'wiek': 39, 'miasto': 'Krakow', 'email': 'adam@gmail.com'}
# del osoba['status'] # KeyError: 'status'

# pop - usuwa po kluczu i zwraca wartosc
wiek = osoba.pop('wiek')
print(osoba)  # {'imie': 'Ala', 'miasto': 'Krakow', 'email': 'adam@gmail.com'}
print(wiek)   # 39

# osoba.pop() # TypeError: pop expected at least 1 argument, got 0
# osoba.pop('wiek') # KeyError: 'wiek'
popik = osoba.pop('wiek','brak')
print(popik)  # brak

# popitem - usuwa ostatnia pare
print(osoba)   # {'imie': 'Ala', 'miasto': 'Krakow', 'email': 'adam@gmail.com'}
ostatni = osoba.popitem()
print(osoba)   # {'imie': 'Ala', 'miasto': 'Krakow'}
print(ostatni) # ('email', 'adam@gmail.com')

# clear() - czysci caly slownik
osoba.clear()
print(osoba) # {}


# Kopiowanie slownikow - ta sama pulapka co z listami

# Zle - obie zmienne wskazuja na ten sam slownik, oryginal zmieniany
a = {'x':1,'y':2}
b = a
b['z'] = 3
print(a)  # {'x': 1, 'y': 2, 'z': 3}

# Dobra kopia
a = {'x':1,'y':2}
b = a.copy() # sposob 1
b = dict(a)  # sposob 2
b['z'] = 3
print(a)  # {'x': 1, 'y': 2}

# Laczenie slownikow
a = {'x':1,'y':2}
b = {'y':99,'z':3}

# operator | laczy dwa slowniki w NOWY slownik, oryginaly bez zmian
# przy tym samym kluczu wygrywa wartosc ze slownika po prawej stronie
# a |= b zmienia slownik a w miejscu
# dziala od Pythona 3.9
c = a | b
print(c)  # {'x': 1, 'y': 99, 'z': 3} y z b, bo b jest po prawej

d = b | a
print(d)  # {'y': 2, 'z': 3, 'x': 1} y z a, bo a jest po prawej

# 9.1 - Stwórz słownik samochod z kluczami: marka, model, rok, kolor. Wyświetl każdą parę klucz-wartość.

samochod = {
    "marka": "Toyota",
    "model": "Corolla",
    "rok": 2022,
    "kolor": "niebieski"
}

for klucz, wartosc in samochod.items():
    print(f"{klucz}: {wartosc}")

# 9.2 - Stwórz słownik oceny = {"Adam": 5, "Ola": 4, "Kasia": 3}. Pobierz ocenę Adama przez [] i
# ocenę Bartka przez .get() z domyślną wartością "brak".

oceny = {"Adam": 5, "Ola": 4, "Kasia": 3}
ocena_adama = oceny["Adam"]
print(f"Ocena Adama: {ocena_adama}")
ocena_bartka = oceny.get("Bartek", "brak")
print(f"Ocena Bartka: {ocena_bartka}")

# 9.3 - Mając słownik magazyn = {"jabłka": 10, "banany": 5, "gruszki": 8}, dodaj "kiwi": 12,
# zmień ilość bananów na 15, usuń gruszki. Wyświetl po każdej operacji.

magazyn = {"jabłka": 10, "banany": 5, "gruszki": 8}
magazyn["kiwi"] = 12
print("Po dodaniu kiwi:", magazyn)
magazyn["banany"] = 15
print("Po zmianie bananów:", magazyn)
del magazyn["gruszki"]
print("Po usunięciu gruszek:", magazyn)

# 9.5 - Mając słownik dane = {"a": 5, "b": 3, "c": 8, "d": 1, "e": 6},
# znajdź klucz z największą wartością i klucz z najmniejszą.

dane = {"a": 5, "b": 3, "c": 8, "d": 1, "e": 6}
klucz_max = max(dane, key=dane.get)
klucz_min = min(dane, key=dane.get)
print("Największa wartość dla klucza:", klucz_max)
print("Najmniejsza wartość dla klucza:", klucz_min)

# 9.8* - Stwórz listę uczniowie, której elementami są słowniki: [{"imie": "Adam", "ocena": 4},
#                                                                {"imie": "Ola", "ocena": 5}, ...].
# Wyświetl tylko uczniów z oceną 5 lub wyższą.

uczniowie = [
    {"imie": "Adam", "ocena": 4},
    {"imie": "Ola", "ocena": 5},
    {"imie": "Kasia", "ocena": 6},
    {"imie": "Tomek", "ocena": 3}
]
for uczen in uczniowie:
    if uczen["ocena"] >= 5:
        print(uczen["imie"], uczen["ocena"])