# ============================================================
# 1. Środowisko pracy
# ============================================================

# https://github.com/szkol23-27/szkol23_27
# Visual Studio Code (microsoft store), albo https://code.visualstudio.com/

# Python --> https://www.python.org/
## ADD python to path

# Pycharm ---> https://www.jetbrains.com/pycharm/



# Przydatne skróty klawiszowe
# Ctrl + /      Wykomentowanie linijki
# Ctrl + C      Kopiowanie do schowka
# Ctrl + V      Wklejanie ze schowka
# Ctrl + S      Zapisz plik
# Ctrl + Z      Cofanie zmian
# Ctrl + Y      Ponowienie zmian (do przodu)
# Ctrl + +      Powiększenie okien
# Ctrl + -      Pomniejszenie okien
# Ctrl + `      Otwarcie / zamknięcie terminala
# Ctrl + \      Podział edytora na dwa okna
# End           Kursor na koniec linii
# Home          Kursor na początek linii
# Tab           Przesuwanie dalej części kodu do przodu
# Shift + Tab   Przesuwanie dalej części kodu do tyłu


# ============================================================
# 2. "Hello world" i pisanie na konsoli
# ============================================================

print('Hello world') # Hello world
print("Hello world") # Hello world
# print('Idziemy na g'mountain') # SyntaxError: unterminated string literal (detected at line 38)
print("Hello world g'mountain") # Hello world g'mountain
print('jeden','dwa','trzeci') # jeden dwa trzeci
print(24) # 24
print(24,56,34) # 24 56 34

# Znaki specjalne
# Znak   Działanie
# \n     Nowa linia
# \t     Tabulator
# \\     Pojedynczy backslash
# \"     Cudzysłów w stringu
# \'     Apostrof w stringu

print('Idziemy na g \' mountain') # Idziemy na g ' mountain
print("Idziemy na g \" mountain") # Idziemy na g " mountain
print('Produkty: \n1.Mleko\n2.Maka')
# Produkty:
# 1.Mleko
# 2.Maka

print('Produkty: \t1.Mleko\t2.Maka') # Produkty:       1.Mleko 2.Maka
print('KOrzystanie \\ tutaj') # KOrzystanie \ tutaj

# Parametr end

print('koniec tutaj',end='')
print('koniec tutaj')
# koniec tutajkoniec tutaj

# parametr sep

print('tutaj maym parametr sep',sep='*') # --> nic sie nie dzieje  # tutaj maym parametr sep
print('tutaj maym parametr sep') # --> nic sie nie dzieje      # tutaj maym parametr sep

print('jeden','dwa','trzeci',sep='*') # jeden*dwa*trzeci


#Ćwiczenie
# 2.2 - Wyświetl imię ulubionej postaci, a w kolejnych liniach: nazwisko, wiek, ulubioną książkę (w cudzysłowie)

print('Geralt \nz Rivii\n150\n"Wiedzmin" by Sapkowski')
#Geralt
# z Rivii
# 150
# "Wiedzmin" by Sapkowski


# 2.3A - Wyświetl dzisiejszą datę w formacie 14/09/2026,
# podając dzień, miesiąc i rok jako trzy osobne wartości w jednym print().
# Kolejny print() ma dopisać w tej samej linii tekst - dzisiaj szkolenie z Pythona (użyj sep)

print(23, 11, 2026, sep="/") # 23/11/2026

print("23", "11", "2026", sep="/", end=" ")
print("dzisiaj szkolenie z Pythona")
# 23/11/2026 dzisiaj szkolenie z Pythona

# Obliczenia na princie
print(2+4)      # 6
print(10-2)     # 8
print(3*7)      # 21
print(10 / 3)   # 3.3333333333333335
print(10 // 3)  # 3
# print(10 / 0) # ZeroDivisionError: division by zero


# obliczenia na str
print("Ala"+" "+"ma") # Ala ma
# print("Banana"-"na") # TypeError: unsupported operand type(s) for -: 'str' and 'str'
# print("Ala"*"str") # TypeError: can't multiply sequence by non-int of type 'str'
print("Ala"*3) # AlaAlaAla
# print("Ala"/"Ala") # TypeError: unsupported operand type(s) for /: 'str' and 'str'
# print("Ala"/3) # TypeError: unsupported operand type(s) for /: 'str' and 'int'

# Zmiana typu
print("Ala" * int("3")) # AlaAlaAla
print("Ala" + str(3))   # Ala3

# 2.4 - Wykonaj w konsoli działanie 3 * 15 * 99 / 121 + 3

print(3 * 15 * 99 / 121 + 3) # 39.81818181818182

# 2.5 - Napraw: print("Teraz mamy przyzwolenie numer" + 593)

print("Teraz mamy przyzwolenie numer"+" "+str(593)) # Teraz mamy przyzwolenie numer 593

# 2.6 - Napraw: print("57" + 35)

print(57+35) # 92

# ============================================================
# 3. Zmienne i typy danych
# ============================================================

# Odniesienie sie do nie istniejacej zmiennej
# print(obliczenie) NameError: name 'obliczenie' is not defined

obliczenie = 3 * 15 * 99 / 121 + 3
print(obliczenie) # 39.81818181818182
obliczenie = 3  # nadpisanie zmiennej, zmiana wartosci
print(obliczenie) # 3

x = 23
y = 34
imie = 'Łukasz'
print(y-x) # 11


# Input proszenie uzyttkowanika o wartosc
"""
imie = input("Podaj swoje imie:")
print(imie)
"""

# input zawsze zwraca str()
""" # Niewspierana operacja int z str
liczba = input("Podaj liczbe:")  # TypeError: unsupported operand type(s) for /: 'str' and 'int'
print(liczba/2)
"""

"""
# Ominiecie problemu # jak wpisze str nadal problem
liczba = int(input("Podaj liczbe:"))
print(liczba/2)
"""

# f-string
age = 18
print(f'Wprowadzamy dane: Wiek:{age}')                  # Wprowadzamy dane: Wiek:18
print(f'Wiek razy dwa {age*2}')                         # Wiek razy dwa 36
print(f'{age} tutaj 1, tutaj 2 {3+2}, tutaj 3 {age*2}') # 18 tutaj 1, tutaj 2 5, tutaj 3 36


# 3.1 - Za pomocą input() zapytaj użytkownika ( o wybrany aspekt) i go wyświetl
"""
imie = input("Jak masz na imię? ")
print("Masz na imię:", imie)
"""

# 3.2* - Za pomocą input() zapytaj o bok a i bok b prostokąta, następnie oblicz pole
"""
a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
pole = a * b
print("Pole prostokąta wynosi:", pole)
"""

# Bool()
# True
# False

test = bool('sdsfdsf')
prawda = True
falsz = False

napis = '' # pusty string (to nie None!)
napis_pelny = 'True'
print(bool(napis))       # False
print(bool(napis_pelny)) # True


# Pulapka zmieniania typow bool()
# bool("False") daje True, bo kazdy niepusty napis jest prawdziwy
# a = bool(input('Napisz True:'))
# print(a)


# Przypiswanie wielu zmiennych naraz
imie, nazwisko = 'damian','poreba'

print(imie,nazwisko) # damian poreba


# Cech zmiennych
# Można przypisać napisy i liczby
# Wielkość liter ma znaczenie (name != Name)
# Nazwy najlepiej po angielsku
# Kilka wyrazów łączymy w jeden ciąg (snake_case)
# Wartość zmiennej jest edytowalna

# Wielkosc = 'sdsdfs'
# print(wielkosc)


# Konwencje nazewnictwa
# Styl         Przykład    Gdzie używany
# snake_case   moje_imie   Zmienne i funkcje w Pythonie
# camelCase    mojeImie    JavaScript
# PascalCase   MojeImie    Nazwy klas w Pythonie


# Dobre praktyki
# wiek                      # jeden wyraz
# first_name                # dwa wyrazy
# liczba_punktow_koncowych  # trzy wyrazy
# gracz1                    # wyraz + cyfra
# total_score_2             # wiele wyrazów + cyfra
# _prywatna_zmienna         # podkreślnik na początku
# max3_proby                # cyfra w środku


# Zle praktyki
# 2gracz          # zaczyna się od cyfry
# imie studenta   # zawiera spację
# średnia_ocen    # polski znak (ś) - technicznie zadziała, ale łamie konwencję (PEP 8)
# moje-imie       # zawiera myślnik
# suma!punktow    # znak specjalny (!)
# class           # słowo zastrzeżone Pythona
# Imie_Studenta   # wielkie litery - w Pythonie zmienne piszemy malymi (snake_case)

import keyword

print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
# 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Typy danych

# Typy danych
# Typ       Opis                        Przykład
# str       Tekst                       "Alicja ma kota"
# int       Liczba całkowita            23, -74
# float     Liczba zmiennoprzecinkowa   25.764, 24.4
# complex   Liczba zespolona            3 + 25j, 25j
# bool      Wartość logiczna            True, False

# zmiennoprzecinkowe zawsze oddzielamy . --> za pomoca przecinka tworzymy cos innego

a,b,c,d,e= 'Alicja',24,57.8,27j,True

print(type(a),type(b),type(c),type(d),type(e)) #<class 'str'> <class 'int'> <class 'float'> <class 'complex'> <class 'bool'>

# Zaokraglanie zmiennoprzecinkowych
zmienno = 6.234543543453
print(round(zmienno,2)) # 6.23
print(round(zmienno,0)) # 6.0
print(round(zmienno,4)) # 6.2345

print(f"{6.234543543453:.2f}") # 6.23
print(f"{6.234543543453:.0f}") # 6
print(f"{6.234543543453:.6f}") # 6.234544

# Zaokraglanie bankierskie
print(round(2.5))            # 2 - a nie 3!
print(round(3.5))            # 4

# Przyklad zaokraglania szkolnego
from decimal import Decimal, ROUND_HALF_UP
print(Decimal("2.5").quantize(Decimal("1"), rounding=ROUND_HALF_UP))  # 3

# 3.4 - Stwórz zmienne: a34 = 10, b34 = 3.14, c34 = "Python", d34 = True. Wyświetl typ każdej z nich za pomocą type().

a34 = 10
b34 = 3.14
c34 = "Python"
d34 = True
print(type(a34)) # <class 'int'>
print(type(b34)) # <class 'float'>
print(type(c34)) # <class 'str'>
print(type(d34)) # <class 'bool'>

# 3.8A - BMI = masa / (wzrost * wzrost). Napisz program, który odbierze od użytkownika jego masę w kilogramach i wzrost
# w metrach, wyliczy i wypisze BMI.
"""
masa = float(input('Podaj masę ciała: '))
wzrost = float(input('Podaj wzrost: '))
BMI = round(masa / (wzrost * wzrost),2)
print(BMI)
"""

# ============================================================
# 4. Instrukcje warunkowe
# ============================================================

# Operatory porownania

# Operatory porównania
# Operator   Znaczenie            Przykład   Wynik
# ==         Równe                5 == 5     True
# !=         Różne (nierówne)     5 != 3     True
# >          Większe              5 > 3      True
# <          Mniejsze             5 < 3      False
# >=         Większe lub równe    5 >= 5     True
# <=         Mniejsze lub równe   3 <= 5     True

x = 10
print(x == 10) # True
print(x != 10) # False
print(x > 5)   # True
print(x >= 10) # True
print(x < 4)   # False
print(x <= 10) # True

# if x == 10: # IndentationError: expected an indented block after 'if' statement on line 334

if x == 10:
    pass # zabezpieczenie, zeby nie wywalilo kodu, ale tez nic nie zrobilo

if x == 10: # True
    print(f'Liczba {x} jest rowna 10') # Liczba 10 jest rowna 10
    print(f'Liczba {x} jest rowna 10') # Liczba 10 jest rowna 10

""" # Blad w cieciu
if x == 10:
    print(f'Liczba {x} jest rowna 10')
    print(f'Liczba {x} jest rowna 10')
print(f'Liczba {x} jest rowna 10')
    print(f'Liczba {x} jest rowna 10') IndentationError: unexpected indent
"""

age = 10

if age >= 18: # False --> nie wykonuje sie
    print('Osoba jest pelnoletnia')


# else
if age >= 18: # False --> wykonuje sie else, bo pomija warunek
    print('Osoba jest pelnoletnia')
else:
    print('osoba jest niepelnoletnia')


grade = 2

if grade == 5: # False --> wykonuje sie else, bo pomija warunek
    print('Zdane')
else:
    print('niezdane')


if grade == 6:     # False --> leci do kolejnego warunku
    print('Masz 6')
elif grade == 5:   # False --> leci do kolejnego warunku
    print('Masz 5')
elif grade == 4:   # False --> leci do else, bo nie ma juz warunkow
    print('Masz 4')
else:              # do else trafia kazda inna ocena (1, 2, 3...), bo else nie sprawdza zadnego warunku
    print('Masz 1') # Masz 1 - mimo ze grade = 2, else wypisze to samo dla kazdej pozostalej oceny



# 4.4 - Poproś użytkownika o temperaturę. Jeśli jest powyżej 30
# - wyświetl Gorąco, jeśli między 15 a 30 -
# Przyjemnie, jeśli poniżej 15 - Zimno.

"""
temp = float(input('Podaj temperature: '))
if temp > 30:
    print('Goraco')
elif temp >= 15:
    print('Przyjemnie')
else:
    print('Zimno')
"""

# 4.5 - Poproś użytkownika o hasło. Jeśli hasło to "admin123"
# - wyświetl Zalogowano, w przeciwnym razie Błędne hasło.

"""
haslo = input("Podaj haslo: ")
if haslo == "admin123":
    print("Zalogowano")
else:
    print("Bledne haslo")
"""

# 4.10A - Rozbuduj swój program do BMI w taki sposób, by poza
# wyświetleniem obliczonego BMI wyświetlił nam również odpowiedni
# opis wg skali z Wikipedii.

"""
masa = float(input('Podaj masę ciała: '))
wzrost = float(input('Podaj wzrost: '))
bmi = round(masa / (wzrost * wzrost),2)

print("Twoje BMI wynosi:", bmi)

if bmi < 16:
    print("Wygłodzenie")
elif bmi < 17:
    print("Wychudzenie")
elif bmi < 18.5:
    print("Niedowaga")
elif bmi < 25:
    print("Prawidłowa masa ciała")
elif bmi < 30:
    print("Nadwaga")
elif bmi < 35:
    print("Otyłość I stopnia")
elif bmi < 40:
    print("Otyłość II stopnia")
else:
    print("Otyłość III stopnia")
"""

# Operatory logiczne w warunkach - and, or, not, is, in


# and  - warunki prawdziwe oba.... -
# or   - jeden warunek prawdziwy... -
# not  - negacje odwrotnosc... -
# is   - najlepszy do sprawdzania, czy jest None... -
# in   - sprawdza czy element jest na liscie,stringu... -

age = 26
prawo_jazdy = True


if age >= 18 and prawo_jazdy: # oba warunki musza sie zgadzac (and)
    print('Jest pelnoletni i posiada prawo jazdy ')


if age < 18 or not prawo_jazdy:
    print('Nie moze prowadzic samochodu')

prawko = False

if not prawko:
    print('Nie ma prawa jazdy')


a = [2,4,5]
b = [2,4,5]
c = a

print(a == b) # True
print(a is b) # False
print(c is a) # True


prawda = None

if prawda is None:
    print('jest')

# Korzystamy z is w przypadku None, Nie uzywajmy zmienna == None


# operator in - sprawdzanie, czy nalezy do
napis = 'Python jest super'

if 'Python' in napis:
    print('Python jest w zmiennej napis')


# 4.6 - Poproś użytkownika o wiek i czy ma bilet (tak/nie). Jeśli ma 18+ i ma bilet -
# wyświetl Wejście dozwolone. W przeciwnym razie Brak wejścia. Użyj and.

"""
wiek = int(input("Podaj swój wiek: "))
bilet = input("Czy masz bilet? (tak/nie): ")
if wiek >= 18 and bilet == "tak":
    print("Wejście dozwolone")
else:
    print("Brak wejścia")
"""

# 4.8 - Poproś użytkownika o imię (może też nic nie wpisać i nacisnąć Enter). Sprawdź
# czy zmienna is not None i czy nie jest pustym stringiem. --> ''
# Jeśli wpisał imię - wyświetl Cześć, [imie]!, jeśli nie - wyświetl Nie podałeś imienia. Użyj operatora is.


"""
imie = input("Podaj swoje imię: ")
if imie == "":      # input() nigdy nie zwraca None - pusty tekst zamieniamy na None sami
    imie = None

if imie is not None:
    print("Cześć,", imie + "!")
else:
    print("Nie podałeś imienia.")
"""


# ============================================================
# 5. Pętle
# ============================================================

# Wykonuje kod bloku dopoki warunek jest prawdziwy

"""
# Nieskonczona petla --> brak warunku wewnatrz petli
while True:
    print('Wykonuje kod bloku')
"""

i = 1
while i <= 5:
    print(i)
    # i = i + 1
    i += 1 # incrementacja

# 1
# 2
# 3
# 4
# 5

"""
odpo = ''
while odpo != 'tak':
    odpo = input("Czy chcesz zakonczyc (tak/nie): ")

print('Koniec programu')

# wyniki
# Czy chcesz zakonczyc (tak/nie): dfsdgffgdgfdgfddfg
# Czy chcesz zakonczyc (tak/nie): fdgfgddfg
# Czy chcesz zakonczyc (tak/nie): dfgfdgdf
# Czy chcesz zakonczyc (tak/nie): fdgdfgd
# Czy chcesz zakonczyc (tak/nie): nie
# Czy chcesz zakonczyc (tak/nie): nie
# Czy chcesz zakonczyc (tak/nie): nie
# Czy chcesz zakonczyc (tak/nie): nie
# Czy chcesz zakonczyc (tak/nie): Tak
# Czy chcesz zakonczyc (tak/nie): Tak 
# Czy chcesz zakonczyc (tak/nie): Takj
# Czy chcesz zakonczyc (tak/nie): Tak 
# Czy chcesz zakonczyc (tak/nie): tak
"""


# Petla for

# range() -> generuje ciag liczb, a petla for wykonuje blok kodu dla kazdej z nich

print(range(1,11)) # zwraca range(1,11) w listach znajdziemy odpowiedz

for i in range(1,11):
    print(i)

print('*'*60)

for i in range(1,11,2):
    print(i)

# range(start, stop, step) - stop nie wchodzi do wyniku
# range(1,11) --> 1,2,3,4,5,6,7,8,9,10
# range(1,11,2) --> 1,3,5,7,9

# krok ujemny range
print('*'*60)

"""
for i in range(1,11,-1): # nic nie wypisze, pusty zakres - przy kroku ujemnym start musi byc wiekszy niz stop, musimy odwrocic kolejnosc start/stop
    print(i)
"""

for i in range(10,0,-1):
    print(i)

print('*'*60)

for i in range(10,-1,-1):
    print(i)

print('*'*60)

napis = 'Python'
for litera in napis:
    print(litera)


# 5.2 - Wyświetl liczby od 10 do 1 (odliczanie w dół) za pomocą pętli while.

licznik = 10
while licznik >= 1:
    print(licznik)
    licznik -= 1
print('*'*60)

# 5.5A - Wyświetl 20 kolejnych potęg liczby 2. 2**i
for pot in range(1, 21):
    print(2 ** pot)
print('*'*60)
# 5.6A - Wydrukuj co 2 liczbę z zakresu 1-50.
for licz in range(1, 51, 2):
    print(licz)
print('*'*60)
# 5.9A - Napisz program będący licznikiem bomby, który korzystając z pętli while
# będzie odliczał od wartości podanej przez użytkownika do 0, po czym wypisze "kaboom!".
"""
licznik = int(input("Podaj liczbe sekund do wybuchu: "))
while licznik >= 0:
    print(licznik)
    licznik -= 1
print("kaboom!")

print('*'*60)
"""

#Zagniezdzanie petli

# 5.11 - Rzucasz dwiema kostkami (każda ma oczka od 1 do 6). Za pomocą dwóch zagnieżdżonych
# pętli for wypisz wszystkie możliwe rzuty, w których suma oczek wynosi 7.

for zewn in range(1,7):
    for wewn in range(1,7):
        if zewn + wewn == 7:
            print(f'{zewn} + {wewn} = 7')


# 5.10 - Wyświetl tabliczkę mnożenia od 1 do 10 (zagnieżdżone pętle). Format: 1 x 1 = 1.

print('*'*60)
for liczba1 in range(1,11):
    for liczba2 in range(1,11):
        print(f"{liczba1} x {liczba2} = {liczba1 * liczba2}")


# - Instrukcja BREAK
# przerywa dzialanie petli pod jakims warunkiem

print('*'*60)
for i in range(1,11):
    print(i)
    if i == 5:
        break


"""
print('*'*60)
while True:
    liczba = int(input("Podaj liczbe (0 = koniec): "))
    if liczba == 0:
        break
    print(f'Wypisales: {liczba}')
"""


# 5.12 - Poproś użytkownika o hasło. Daj mu maksymalnie 3 próby.Jeśli wpisze poprawne ("admin123")
# - wyświetl Zalogowano i przerwij pętlę (break). Jeśli nie trafi - Brak prób.


""" # 1 sposob rozwiazania
pozostale_proby = 3
while pozostale_proby > 0:
    password = input("Podaj haslo (max 3 proby): ")
    if password == "admin123":
        print("Zalogowano")
        break
    else:
        pozostale_proby -= 1
        print(f"Bledne haslo. Pozostalo {pozostale_proby} prob")
"""

""" # 2 sposob rozwiazania
proby = 3
zalogowany = False
while proby > 0:
    haslo = input("Podaj haslo (max 3 proby): ")
    if haslo == "admin123":
        print("Zalogowano")
        zalogowany = True
        break
    proby -= 1

if not zalogowany:
    print("Brak prob.")
"""

print('*'*60)
print('Operator modulo')
print('*'*60)
# Operator % (modulo) - reszta z dzielenia
# zwraca reszte z dzielenie jednej liczby przez druga

print(10%3) # 1
print(10%2) # 0
print(7%2)  # 1


# Sprawdzenie, czy liczba jest parzysta
print(10 % 2 == 0) # True
print(9 % 2 == 0)  # False

# Sprawdzenie, czy liczba jest nieparzysta
if 9 % 2 == 1:
    print('Mamy tutaj nieparzysta')


# - Instrukcja CONTINUE
print('*'*60)
for i in range(1,11): #1,2,3,4,5,6,7,8,9,10
    if i % 2 == 0:
        continue
    print(i)


print('*'*60)

i = 0
while i < 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1


# 5.15A - Wydrukuj liczby w zakresie 1-100, wypisując obok, czy dana liczba jest parzysta czy nieparzysta.
for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} - parzysta")
    else:
        print(f"{i} - nieparzysta")


print('*'*60)

# 5.16 - Wypisz wszystkie liczby z zakresu 1-50, które dzielą się jednocześnie przez 3 i przez 5. Użyj operatora %.
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


print('*'*60)

# 5.17 - Wyświetl wszystkie liczby od 1 do 20, ale pomiń (continue) te, które dzielą się przez 3.
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

print('*'*60)

# 5.19* - Mając napis tekst = "Programowanie w Pythonie", wypisz w jednej linii wszystkie jego znaki oprócz samogłosek
# (a, e, i, o, u, y) i spacji. Pomijaj je za pomocą continue. Wielkość liter ma nie mieć znaczenia.

txt = "Programowanie w Pythonie"

# Wersja z bledem - nie pomija wielkich samoglosek (A, E, O...)
for sign in txt:
    if sign in "aeiouy ":
        continue
    print(sign, end="")
print('') # PrgrmwnwPthn - tu dziala, bo w tekscie nie ma wielkiej samogloski

# Pokazanie bledu na tekscie z wielkimi samogloskami
for sign in "Ola i Ewa":
    if sign in "aeiouy ":
        continue
    print(sign, end="")
print('') # OlEw - zostaly wielkie O i E, a nie powinny

# Wersja poprawiona - sign.lower() zamienia znak na maly przed sprawdzeniem
for sign in txt:
    if sign.lower() in "aeiouy ":
        continue
    print(sign, end="")
print('') # PrgrmwnwPthn

for sign in "Ola i Ewa":
    if sign.lower() in "aeiouy ":
        continue
    print(sign, end="")
print('') # lw - wielkie samogloski tez pominiete

# ============================================================
# 6. Łańcuchy znaków
# ============================================================

# upper(), lower(), title(), capitalize(), swapcase()

# metody i funkcje
# funkcje  powitanie(....)
# metody   zmienna.lower()

tekst = 'Witaj w pYthOnie'

print(tekst.upper())        # WITAJ W PYTHONIE # wszystkie litery na duze
print(tekst.lower())        # witaj w pythonie # wszystkie litery na male
print(tekst.title())        # Witaj W Pythonie # wszystkie litery rozpoczynajace slowa na duze, reszta liter na male
print(tekst.capitalize())   # Witaj w pythonie # ustawia tylko 1 litere na duza, reszta liter na male
print(tekst.swapcase())     # wITAJ W PyTHoNIE # ustawia wszystkie male na duze i wszystkie duze na male


haslo = "Admin123"
if haslo.lower() == "admin123":
    print("Zalogowano")

# replace()

tekst = 'Lubie koty i koty lubia mnie'

# zamienia wszystkie wystapienia 'koty' na 'psy'
print(tekst.replace("koty","psy")) # Lubie psy i psy lubia mnie

# zamien tylko pierwsze wystapianie (trzeci parametr, ile)
print(tekst.replace("koty",'psy',1)) # Lubie psy i koty lubia mnie

# zamien tylko pierwsze 2 wystapiania (trzeci parametr, ile)
print(tekst.replace("koty",'psy',2)) # Lubie psy i psy lubia mnie

# odporne na bledy (trzeci parametr) - gdy liczba jest wieksza niz liczba wystapien, zamienia wszystkie i nie zglasza bledu
print(tekst.replace("koty",'psy',6)) # Lubie psy i psy lubia mnie


# Wykorzystanie przykladowe. Usuniecie spacji z lancucha znakow
email = "  adam @ mail . com"
print(email.replace(" ","")) # adam@mail.com

# - len w kontekście ciągów tekstowych

tekst = 'Hello world'
print(len(tekst))            # 11 - spacja sie tez liczy

print(len(""))               # 0 - pusty string
print(len("Python\n"))       # 7 - znak specjalny liczy jako 1
print(len(" "))              # 1 - sama spacja to tez znak
print(len('Ala ma ko\tta'))  # 12 - tabulator to znak specjalny
print(len('śś'))             # 2 polskie znaki po jednym

"""
haslo = input('Podaj haslo: ')
if len(haslo) < 8:
    print('haslo jest za krotkie')
"""

