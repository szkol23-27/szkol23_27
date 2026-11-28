# ============================================================
# 10. Zbiory
# ============================================================

# Tworzenie zbiorów i konwersje z innych typów złożonych

# Jest to nieuporzadkowana kolekcja unikalnych elementow

pusty = set()
print(type(pusty)) # <class 'set'>
pusty2 = {} # {} to pusty slownik, nie zbior
print(type(pusty2)) # <class 'dict'>

# zbior z elementami
owoce = {'jablko','banan','gruszka','wisnia','banan'}
print(type(owoce)) # <class 'set'>
print(owoce) # {'gruszka', 'wisnia', 'jablko', 'banan'}

# duplikaty sa automatycznie usuwane
liczby = {1,2,3,4,5,6,1,4,3,5,6,2}
print(liczby) # {1, 2, 3, 4, 5, 6}

print({2.5, 6.2, 3.8, 2.5, 6.7}) # {2.5, 3.8, 6.2, 6.7}
print({True,False,True,False})   # {False, True}

# Konwersje z innych typow

# lista -> zbior
lista = [1,3,2,4,4,2,4,2,6,5,4,2]
print(lista)               # [1, 3, 2, 4, 4, 2, 4, 2, 6, 5, 4, 2]
print(set(lista))          # {1, 2, 3, 4, 5, 6}
lista_secik = set(lista)
print(list(lista_secik))   # [1, 2, 3, 4, 5, 6]

# krotki -> zbior
krotka = (10,20,30,40,20,10,40)
print(krotka)       # (10, 20, 30, 40, 20, 10, 40)
print(set(krotka))  # {40, 10, 20, 30}

# string -> zbior (kazda litera osobno)
litery = 'banana'
print(litery)       # banana
print(set(litery))  # {'a', 'b', 'n'}

# slownik -> zbior
dane = {"a":1,"b":2,"c":3}
print(dane)                 # {'a': 1, 'b': 2, 'c': 3}
print(set(dane))            # {'b', 'c', 'a'}
print(set(dane.values()))   # {1, 2, 3}

# sorted() na zbiorach

litery = set('abrakadabra')
print(litery) # {'k', 'r', 'd', 'b', 'a'}

# .sort metoda tylko na listach, przy set wywali nam blad
# litery.sort() # AttributeError: 'set' object has no attribute 'sort'

# Przy sorted zmienia nam na listy, ale przy powrocie na set drugi raz nam ustawia po swojemu nasze elementy
print(sorted(litery))      # ['a', 'b', 'd', 'k', 'r']
print(set(sorted(litery))) # {'d', 'b', 'r', 'a', 'k'}


# Liczby - zbior nie miesza losowo, ale tez nie sortuje
print(set([5,3,1]))     # {1, 3, 5} # wyglada na sortowanie
print(set([10,3,7]))    # {10, 3, 7}


# 10.1 - Utwórz po jednej zmiennej każdego z poniższych typów, a następnie na ich podstawie utwórz odpowiadający im zbiór (set):

#     string (dowolny tekst, np. z powtarzającymi się literami) → zbiór unikalnych liter
#     int → zastanów się, czy set() zadziała bezpośrednio na pojedynczej liczbie (spróbuj i sprawdź, co się stanie)
#     lista (z kilkoma powtarzającymi się elementami) → zbiór bez duplikatów
#     krotka (z kilkoma powtarzającymi się elementami) → zbiór bez duplikatów
#     słownik (przynajmniej 3 pary klucz-wartość) → jeden zbiór zrobiony z kluczy, drugi osobny zbiór zrobiony z wartości (.values())

# Dla każdego przypadku wypisz na konsoli zarówno zmienną oryginalną, jak i wynikowy zbiór, żeby zobaczyć różnicę.

zmienna_tekstowa = 'mississippi'
print(zmienna_tekstowa)         # mississippi
print(set(zmienna_tekstowa))    # {'m', 'i', 's', 'p'} # kolejnosc liter moze byc inna przy kazdym uruchomieniu

zmienna_calkowita = 25
# print(set(zmienna_calkowita)) # TypeError: 'int' object is not iterable
print(set([zmienna_calkowita])) # {25} # liczbe trzeba najpierw wlozyc do listy

zmienna_lista = [1, 2, 2, 3, 3, 3, 4]
print(zmienna_lista)            # [1, 2, 2, 3, 3, 3, 4]
print(set(zmienna_lista))       # {1, 2, 3, 4}

zmienna_krotka = (5, 6, 6, 7, 5)
print(zmienna_krotka)           # (5, 6, 6, 7, 5)
print(set(zmienna_krotka))      # {5, 6, 7}

zmienna_slownik = {'x': 1, 'y': 2, 'z': 1}
print(zmienna_slownik)                  # {'x': 1, 'y': 2, 'z': 1}
print(set(zmienna_slownik))             # {'x', 'y', 'z'} # kolejnosc moze byc inna
print(set(zmienna_slownik.values()))    # {1, 2}

# 10.2 - Mając string "abrakadabra", znajdź ile unikalnych liter zawiera i wyświetl je posortowane.

tekst = "abrakadabra"
unikalne = set(tekst)
print(f"Unikalnych liter jest {len(unikalne)}")
print(f"Litery: {sorted(unikalne)}")


# Modyfikowanie zawartości zbiorów

# Dodawanie elementow do zbioru
# add() update()

imiona = {'Ala','Dominik'}

# add - dodaj jeden element do zbioru
imiona.add('Kamil')
print(imiona) # {'Dominik', 'Kamil', 'Ala'}

# dodanie istniejacego elementu - nic sie nie dzieje
imiona.add('Ala')
print(imiona) # {'Kamil', 'Dominik', 'Ala'}

# update - dodawanie wiele elementow w jednym momencie
imiona.update(['Jaroslaw','Konrad'])
print(imiona) # {'Kamil', 'Ala', 'Jaroslaw', 'Dominik', 'Konrad'}

# update() pozwala na kazda kolekcje, czyli lista, krotka , slownik, inny zbior
owoce = {'jablko'}
owoce.update(['jablko','wisnia'])
owoce.update(('agrest','wisnia'))
owoce.update({'czeresnia'})
owoce.update({'a':'pomarancza','b':'orzechy'}.values())
print(owoce) # {'pomarancza', 'czeresnia', 'orzechy', 'wisnia', 'agrest', 'jablko'}

owoce.update('dsfdsfdfs','dsfsdffsd') # kilka argumentow naraz, kazdy string rozbija sie na pojedyncze litery
owoce.update('kanapka') # doda litery k a n p, a nie cale slowo 'kanapka'
# owoce.update(23) # TypeError: 'int' object is not iterable
print(owoce) # oprocz owocow sa tez pojedyncze litery: 'd', 's', 'f', 'k', 'a', 'n', 'p'

# Usuwanie elementow w zbiorze
# remove() discard() pop() clear()

jezyki = {"Python",'Java','C++','Rust','Go'}

# remove() - usuwa element
jezyki.remove("Java")
print(jezyki) # {'Go', 'Rust', 'Python', 'C++'}
# jezyki.remove('Java') # KeyError: 'Java'

# discard()- usuwa element ( bez bledu jesli element nie istnieje w zbiorze )
jezyki.discard('Rust')
jezyki.discard('Rust') # ok, nic sie nie stanie
print(jezyki) # {'C++', 'Python', 'Go'}

# pop() - usuwa i zwraca dowolny element (nie wiadomo ktory, ale to nie losowanie)
usuniety = jezyki.pop()
print(f'Usunieto: {usuniety}') # Usunieto: "?" # nie da sie przewidziec ktory element wypadnie
# jezyki.pop(0) # TypeError: set.pop() takes no arguments (1 given)

# clear - czysci caly zbior
jezyki.clear()
print(jezyki) # set() - pusty zbior

# Sprawdzenie obecnosci
# zbiory najszybsze do sprawdzania obecnosci
duzy_zbior = set(range(1,500))

print(20 in duzy_zbior)         # True
print(200000 in duzy_zbior)     # False

# 10.3 - Masz kolory = {"czerwony", "zielony"}. Dodaj przez update()
# listę ["niebieski", "zielony", "żółty"]. Wyświetl zbiór i jego długość.

kolory = {"czerwony", "zielony"}
kolory.update(["niebieski", "zielony", "żółty"])
print(kolory)
print(f'Zbior kolory posiada {len(kolory)} elementow')

# 10.4 - Masz wolne miejsca w kinie wolne = {"A1", "A2", "A3", "B1"}.
# Zapytaj użytkownika o miejsce. Jeśli jest wolne, usuń je i wypisz Zarezerwowano.
# Jeśli nie, wypisz Miejsce zajęte.

"""
wolne = {"A1", "A2", "A3", "B1"}
pytanie = input('Jakie miejsce chcesz zarezerwowac: ')

if pytanie.upper() in wolne:
    wolne.discard(pytanie.upper())
    print(f'Zarezerwowano {pytanie.upper()}')
else:
    print('Miejsce zajęte')
"""

"""
wolne = {"A1", "A2", "A3", "B1"}
miejsce = input("Podaj miejsce: ")
if miejsce in wolne:
    print('Zarezerwowano')
    wolne.remove(miejsce)
    print(f'Wolne: {wolne}')
else:
    print("Miejsce zajete")
    print(f'Wolne: {wolne}')
"""

# difference --> roznice
# za pomoca .difference() lub operatora - wypisac elementy ktore sa w pierwszy zbiorze, ale nie ma ich w drugim

a = {1,2,3,4,5}
b = {4,5,6,7,8}

# elementy w a, ktorych nie ma w b
print(a.difference(b)) # {1, 2, 3}
print(a - b)           # {1, 2, 3}

# elementy w b, ktorych nie ma w a
print(b.difference(a)) # {8, 6, 7}
print(b - a)           # {8, 6, 7}

# symmetric_difference - elementy w a LUB b, ale nie w obu
print(a.symmetric_difference(b)) # {1, 2, 3, 6, 7, 8}
print(a ^ b)                     # {1, 2, 3, 6, 7, 8}

# Praktyczny przyklad
wszyscy = {'Adam','Roman','Kamil','Zofia','Ola'}
oddali = {'Ola','Adam','Kamil'}

nie_oddali = wszyscy - oddali
print(f'Nie oddali pracy: {nie_oddali}')

# 10.5 - Sam stwórz dwa zbiory uczestników warsztatów: dzien1 i dzien2, z własnymi imionami. Warunki:

#     w każdym zbiorze co najmniej 5 osób,
#     co najmniej 2 osoby muszą być w obu zbiorach (były na warsztatach oba dni) - bez wspólnych osób zadanie nie ma sensu.

# Znajdź: kto był tylko pierwszego dnia, kto był tylko drugiego dnia, oraz kto był tylko w jednym z dwóch dni (czyli nie wziął udziału w obu naraz).

dzien1 = {'Adam', 'Ola', 'Kamil', 'Zofia', 'Bartek'}
dzien2 = {'Ola', 'Kamil', 'Marta', 'Piotr', 'Ewa'}

print(f'Tylko pierwszego dnia: {dzien1 - dzien2}') # Adam, Zofia, Bartek
print(f'Tylko drugiego dnia: {dzien2.difference(dzien1)}') # Marta, Piotr, Ewa
print(f'Tylko w jednym z dni: {dzien1 ^ dzien2}') # wszyscy oprocz Oli i Kamila


# intersection -> czesc wspolna
# intersection() lub operator & --> elementy ktore wystepuja w obu zbiorach

a = {1,2,3,4,5}
b = {4,5,6,7,8}

print(a.intersection(b))  # {4, 5}
print(a & b)              # {4, 5}

c = {5,7,6}
print(a & b & c) # {5}
print(a.intersection(b,c))

# Praktyczny przyklad

# wspolne zainteresowanie
adam = {'gory','wycieczki','czytanie','filmy'}
janek = {'czytanie','snowboard','wino'}

wspolne = adam & janek
print(f'Wspolne zainteresowania adama i janka {wspolne}')

# 10.6 - Sam stwórz dwa zbiory: moje_filmy z Twoimi ulubionymi filmami i filmy_kolegi z ulubionymi filmami kolegi lub koleżanki. Warunki:

#     w każdym zbiorze co najmniej 5 filmów,
#     co najmniej 2 filmy muszą być w obu zbiorach - bez wspólnych filmów zadanie nie ma sensu.

# Znajdź filmy, które lubicie oboje - raz przez intersection(), raz operatorem &. Wyświetl też, ile ich jest.

moje_filmy = {"Skazani na Shawshank", "Zielona mila","Pulp Fiction","Incepcja","Diuna"}
filmy_kolegi = {"Skazani na Shawshank", "Zielona mila","Ojciec chrzestny","Matrix","Forrest Gump"}

print(f'Ulubione filmy to: {moje_filmy.intersection(filmy_kolegi)}')
wspolne = moje_filmy & filmy_kolegi
print(f'Ulubione filmy to: {wspolne}')
print(f'Wspolnych filmow jest: {len(wspolne)}') # Wspolnych filmow jest: 2


# union

a = {1,2,3,4,5}
b = {4,5,6,7,8}

print(a.union(b)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(a | b)      # {1, 2, 3, 4, 5, 6, 7, 8}

c = {10,20}

print(a | b | c)       # {1, 2, 3, 4, 5, 6, 7, 8, 10, 20}
print(a.union(b, c))   # {1, 2, 3, 4, 5, 6, 7, 8, 10, 20}


# 10.7 - Tagi w albumie ze zdjęciami. Masz dwa zdjęcia z wakacji:

#     zdjęcie 1 - słoneczna plaża,
#     zdjęcie 2 - słoneczne góry z widokiem na Morskie Oko.

# Wymyśl sam tagi pasujące do każdego zdjęcia (co najmniej 4 na zdjęcie) i
# zapisz je w dwóch zbiorach: zdjecie1 i zdjecie2.
# Część tagów będzie pasować do obu zdjęć - użyj ich w obu zbiorach.
# Za pomocą union() albo | wypisz posortowane wszystkie tagi albumu
# bez powtórzeń oraz ile ich jest.

zdjecie1 = {"plaża", "lato", "morze", "słońce", "wakacje"}
zdjecie2 = {"Morskie Oko", "słońce", "góry", "wakacje", "lato"}
print("Tagi zdjęcia 1:", zdjecie1)
print("Tagi zdjęcia 2:", zdjecie2)
print("Wszystkie tagi (posortowane):", sorted(zdjecie1.union(zdjecie2)))
print("Liczba unikalnych tagów:", len(zdjecie1 | zdjecie2))

# Inne przydatne metody zbiorow
a = {1,2,3}
b = {1,2,3,4,5}
c = {6,7}

# issubset - czy a jest podzbiorem b
print(a.issubset(b)) # True
print(a <= b)        # True

# issuperset - czy b jest nadzbiorem
print(b.issuperset(a))  # True
print(b >= a)           # True

# isdisjoint - czy zbiory nie maja wspolnych elementow
print(a.isdisjoint(c)) # True
print(a.isdisjoint(b)) # False

# frozenset - niezmienny zbior
zamrozony = frozenset([1,2,3,4,5,6])
# zamrozony.add(78) # AttributeError: 'frozenset' object has no attribute 'add'
print(zamrozony)


# ============================================================
# 11. Zaawansowane przetwarzanie list i zbiorow
# ============================================================

# List comprehension
# tworzenie listy w jednej linijce kodu

#zwykly sposob - petla
kwadraty = []
for i in range(1,6):
    kwadraty.append(i**2)
print(kwadraty)     # [1, 4, 9, 16, 25]

# list comprehension - to samo w jednej linijce
kwadraty = [i**2 for i in range(1,6)]
print(kwadraty)    # [1, 4, 9, 16, 25]

# z warunkiem - tylko parzyste 10 % 2 == 0
parzyste = [i for i in range(1,21) if i % 2 == 0]
print(parzyste) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# transformacja - zamien parzyste na "P", nieparzyste na "N"
wynik = ["P" if x % 2 == 0 else "N" for x in range(1,11)]
print(wynik)  # ['N', 'P', 'N', 'P', 'N', 'P', 'N', 'P', 'N', 'P']

wynik = [x**2 for x in range(1,11) if x % 2 == 0]
print(wynik)  # [4, 16, 36, 64, 100]

# splaszczenie macierzy (lista list --> jedna zwykla lista) - zagniezdzone comprehension
# czytamy jak dwa fory: for mac in macierz, a w srodku for element in mac
macierz = [[1,2,3],[2,3,4],[3,4,5]]
plaska = [element for mac in macierz for element in mac]
print(plaska) # [1, 2, 3, 2, 3, 4, 3, 4, 5]


# set comprehension - tworzenie zbiorow w jednej lini

# kwadraty liczb od 1 do 10
kwadraty = {x ** 2 for x in range(1,11)}
print(kwadraty) # {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}

# unikalne dlugosci slow
slowa = ['kot','dominik','pies','zaba','osa']
dlugosci = {len(s) for s in slowa}
print(dlugosci) # {3, 4, 7}

# slowniki comprehension
kwadraty = {x: x ** 2 for x in range(1,6)}
print(kwadraty) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

original = {"a":1,"b":2,"c":3}
odwrocony = {value: key for key,value in original.items()}
print(odwrocony) # {1: 'a', 2: 'b', 3: 'c'}

# dict co z filtrem
oceny = {"adam":5,'ola':2,'Kasia':4,'Bartek':3,'zofia':6}
najlepsi = {key:value for key,value in oceny.items() if value >= 4}
print(najlepsi) # {'adam': 5, 'Kasia': 4, 'zofia': 6}

# 11.1 - Mając listę temperatur [-5, 12, 0, 25, -2, 18, 30, -10], użyj list comprehension z if/else,
# żeby zamienić każdą wartość na etykietę: "zimno" (poniżej 15) lub "ciepło" (15 i więcej).

temperatury = [-5, 12, 0, 25, -2, 18, 30, -10]
etykiety = ["zimno" if t < 15 else "ciepło" for t in temperatury]
print(etykiety)

# 11.2 - Mając listę liczb [4, 7, 2, 9, 15, 3, 22, 11, 8], jednym list comprehension (filtrowanie + transformacja razem)
# stwórz nową listę zawierającą podwojone wartości, ale tylko tych liczb, które są większe od 5.

liczby = [4, 7, 2, 9, 15, 3, 22, 11, 8]
podwojone = [x*2 for x in liczby if x > 5]
print(podwojone) # [14, 18, 30, 44, 22, 16]

# 11.3 - Mając listę słów ["kot", "słoń", "hipopotam", "mysz", "żyrafa", "ryś"], użyj dict comprehension,
# żeby stworzyć słownik, w którym kluczem jest słowo, a wartością jego długość - ale tylko dla słów dłuższych niż 3 litery

slowa = ["kot", "słoń", "hipopotam", "mysz", "żyrafa", "ryś"]
compr = {x:len(x) for x in slowa if len(x) > 3}
print(compr) # {'słoń': 4, 'hipopotam': 9, 'mysz': 4, 'żyrafa': 6}

# map() stosuje funkcje do kazdego elementu
liczby = [1,2,3,4,5]
# map(funkcja, dane) --> funkcja odpalana na kazdym elemencie
# lambda x: x * 2 to po prostu ta funkcja, x to kolejny element z listy
podwojone = map(lambda x: x * 2,liczby)
print(podwojone) # <map object at 0x72daaa4c59c0> # map nie daje listy, trzeba opakowac w list()
podwojone = list(map(lambda x: x * 2,liczby))
print(podwojone) # [2, 4, 6, 8, 10]

# map, wiele list
a = [1,2,3]
b = [10,20,30]
sumy = list(map(lambda x, y: x+y, a, b))
print(sumy) # [11, 22, 33]

# filter() filtruje
liczby = [1,2,3,4,5]
parzyste = filter(lambda x: x % 2 == 0,liczby)
print(parzyste)  # <filter object at 0x744c277d48e0>
parzyste = list(filter(lambda x: x % 2 == 0,liczby))
print(parzyste) # [2, 4]

slowa = ["kot", "słoń", "hipopotam", "mysz", "żyrafa", "ryś", 'sowa']
dlugie = list(filter(lambda s: len(s) > 4, slowa))
print(dlugie) # ['hipopotam', 'żyrafa']

# filtrowanie listy slownikow

produkty = [
    {'nazwa':"laptop","cena":6000},
    {'nazwa':"Mysz","cena":100},
    {'nazwa':"Monitor","cena":2000},
    {'nazwa':"pad","cena":300}
]

drogie = list(filter(lambda p: p['cena'] > 500,produkty))
print(drogie) # [{'nazwa': 'laptop', 'cena': 6000}, {'nazwa': 'Monitor', 'cena': 2000}]

# 11.4 - Mając dwie listy: ceny = [100, 250, 80] i rabaty = [10, 50, 5], użyj map(),
# żeby policzyć ceny po rabacie (cena - rabat) dla każdej pary naraz.

ceny = [100, 250, 80]
rabaty = [10, 50, 5]
po_r = list(map(lambda cena, rabat: cena - rabat, ceny, rabaty))
print(po_r) # [90, 200, 75]

# 11.5 - Mając listę słowników osoby = [{"imie": "Adam", "wiek": 17}, {"imie": "Ola", "wiek": 22},
#                                {"imie": "Kasia", "wiek": 15}, {"imie": "Bartek", "wiek": 30}],
# użyj filter(), żeby zostawić tylko osoby pełnoletnie (wiek >= 18).

osoby = [{"imie": "Adam", "wiek": 17},
         {"imie": "Ola", "wiek": 22},
         {"imie": "Kasia", "wiek": 15},
         {"imie": "Bartek", "wiek": 30}
         ]

pelnoletnie = list(filter(lambda p: p["wiek"]>=18, osoby))
print(pelnoletnie) # [{'imie': 'Ola', 'wiek': 22}, {'imie': 'Bartek', 'wiek': 30}]


# sorted() key

# sortowanie str po dlugosci
slowa = ['Python','Java','Javascript','C','Rust']
print(sorted(slowa, key=len)) # ['C', 'Java', 'Rust', 'Python', 'Javascript']

# sortowanie bez uwzglednienia wielkosci liter
imiona = ['Zofia','Adam','kasia','ola','Bartek']
print(sorted(imiona, key=str.lower)) # ['Adam', 'Bartek', 'kasia', 'ola', 'Zofia']
# key=str.lower bez nawiasow --> dajemy sama funkcje, sorted sam ja odpali dla kazdego imienia
# key=str.lower() z nawiasami --> TypeError, bo funkcja odpala sie od razu i nie ma na czym zadzialac

# sortowanie listy slownikow
uczniowie = [{"imie": "Adam", "ocena": 1},
         {"imie": "Ola", "ocena": 4},
         {"imie": "Kasia", "ocena": 5},
         {"imie": "Bartek", "ocena": 3}
         ]

print(sorted(uczniowie,key=lambda u: u['ocena'],reverse=True))
# [{'imie': 'Kasia', 'ocena': 5}, {'imie': 'Ola', 'ocena': 4}, {'imie': 'Bartek', 'ocena': 3}, {'imie': 'Adam', 'ocena': 1}]


# sortowanie po wielu kryteriach
dane = [('Adam',4),('Rafal',5),('Agnieszka',5),('Maciej',1)]

print(sorted(dane,key=lambda x:(-x[1],x[0])))
# [('Agnieszka', 5), ('Rafal', 5), ('Adam', 4), ('Maciej', 1)]


# 11.6 - Masz listę imion: imiona = ["Bartek", "Zo", "Kasia", "Ala", "Krzysztof"].
# Posortuj ją od najkrótszego do najdłuższego imienia.

imiona = ["Bartek", "Zo", "Kasia", "Ala", "Krzysztof"]
print(sorted(imiona,key=len)) # ['Zo', 'Ala', 'Kasia', 'Bartek', 'Krzysztof']


# sortowania wieloprzebiegowego
ludzie = [
    {"imie": "Jan",   "nazwisko": "Abacki",    "wiek": 30, "pensja": 7000, "miasto": "Gdansk"},
    {"imie": "Anna",  "nazwisko": "Kowalska",  "wiek": 30, "pensja": 5000, "miasto": "Krakow"},
    {"imie": "Adam",  "nazwisko": "Kowalski",  "wiek": 30, "pensja": 6000, "miasto": "Krakow"},
    {"imie": "Adam",  "nazwisko": "Kowalski",  "wiek": 30, "pensja": 5500, "miasto": "Krakow"},
    {"imie": "Ola",   "nazwisko": "Nowak",     "wiek": 25, "pensja": 4000, "miasto": "Krakow"},
    {"imie": "Ewa",   "nazwisko": "Zielinska", "wiek": 30, "pensja": 7000, "miasto": "Gdansk"},
]

# # kryteria musimy obrocic
# ludzie.sort(key=lambda o: o['imie'])                    # kryterium najmniej wazne
# ludzie.sort(key=lambda o: o['pensja'],reverse=True)
# ludzie.sort(key=lambda o: o['nazwisko'])
# ludzie.sort(key=lambda o: o['wiek'],reverse=True)
# ludzie.sort(key=lambda o: o['miasto'])                  # kryterium najwazniejsze

# sortujemy po kolei kilka razy, kazdy raz po czym innym
# przy takich samych wartosciach sort nie miesza tego co bylo wczesniej
# czyli ostatni sort jest najwazniejszy --> tu imie, potem pensja, nazwisko, wiek, miasto
ludzie.sort(key=lambda o: o['miasto'])
ludzie.sort(key=lambda o: o['wiek'],reverse=True)
ludzie.sort(key=lambda o: o['nazwisko'])
ludzie.sort(key=lambda o: o['pensja'],reverse=True)
ludzie.sort(key=lambda o: o['imie'])


for i in ludzie:
    print(i)


# any() all() sprawdzanie kolekcji

liczby = [1,2,3,4,5,6,7,8]

# any --> czy jakikowliek element z listy jest parzysty
print(any(x % 2 == 0 for x in liczby)) # True

# all() --> czy wszystkie sa dodatnie
print(all(x > 0 for x in liczby))       # True
# all() --> czy wszystkie sa wieksze niz 3
print(all(x > 3 for x in liczby))       # False


# ============================================================
# 12. Wyjatki i obsluga bledow
# ============================================================

# Wyjatek to blad ktory pojawia sie podczas dzialania programu

# dzielenie przez 0

# wynik = 10 / 0 # ZeroDivisionError: division by zero

# try/except

try:
    wyniki = 10 / 0
except:
    print('Wystapil blad')

print('Program dziala dalej')


# lapanie wyjatkow - konkretny przypadek
# ZeroDivisionError # ValueError

"""
try:
    liczba = int(input('Podaj liczbe: '))
    wynik = 100 / liczba
    print(f'Wynik: {wynik}')
except ZeroDivisionError:
    print('Nie mozna dzielic przez zero')
except ValueError:
    print('To nie jest liczba!')
"""

"""
try:
    liczba = int(input('Podaj liczbe: '))
    wynik = 100 / liczba
    print(f'Wynik: {wynik}')
except ValueError, ZeroDivisionError: # dziala od pythona 3.14, nizej trzeba w krotce --> except (ValueError, ZeroDivisionError):
    print('Wystapil blad')
"""


# 12.1 - Masz listę zakupów produkty = ["chleb", "mleko", "jajka"]. Napisz program, który pyta użytkownika o numer produktu
# (licząc od 1) i wyświetla jego nazwę. Obsłuż osobno dwa przypadki:
# użytkownik wpisał coś, co nie jest liczbą (ValueError), oraz podał numer spoza zakresu listy (IndexError).

"""
produkty = ["chleb", "mleko", "jajka"]
try:
    nr_produktu = (int(input('Podaj numer produktu: ')))
    if nr_produktu < 1: # bez tego 0 dalby produkty[-1], czyli ostatni produkt zamiast bledu
        raise IndexError
    print (produkty[nr_produktu -1])
except ValueError:
    print("Musisz podać liczbę!")
except IndexError:
    print("Nie ma produktu o takim numerze!")
"""

"""
# try/except/else/finally
try:
    liczba = int(input('Podaj liczbe: '))
    wynik = 100 / liczba
except ZeroDivisionError:
    print('Nie mozna dzielic przez zero')
except ValueError:
    print('To nie jest liczba!')
else:                                       # tylko gdy nie bylo bledu
    print(f'Wynik: {wynik}')
finally:                                    # zawsze sie wykona
    print('Koniec operacji')
"""

# Typowe bledy
# ZeroDivisionError -> dzielenie przez zero           --> print(10 / 0)
# ValueError        -> dobry typ, ale zla wartosc     --> int('abc')
# TypeError         -> operacja na niezgodnych typach --> print('tekst' + 5)
# IndexError        -> indeks poza zakresem listy     --> lista = [2,3] print(lista[20])
# KeyError          -> brak klucza w slowniku         --> slownik = {} print(slownik['klucz'])
# FileNotFoundError -> brak pliku, nie istnieje       --> open('dane.txt')
# NameError         -> brak takiej zmiennej           --> print(okoliczne_zmienne)
# SyntaxError       -> blad skladniowy, np. brak :    --> if x == 5
# IndentationError  -> zle wciecie (odmiana SyntaxError)
#                      tych dwoch try nie zlapie, Python sprawdza skladnie przed uruchomieniem pliku


# as e
try:
    int('abc')
except ValueError as e:
    print(f'Typ bledu: {type(e).__name__}') # Typ bledu: ValueError
    print(f'Komunikat: {e}')                # Komunikat: invalid literal for int() with base 10: 'abc'


# raise swoj wlasny wyjatek
wiek = 200

try:
    if wiek < 0:
        raise ValueError('Wiek nie moze byc ujemny')
    if wiek > 150:
        raise ValueError('Wiek nie moze przekraczac 150!')
except ValueError as e:
    print(e)


# 12.2 - Mając listę dane = [10, 20, 30], spróbuj pobrać element o indeksie 10. Obsłuż IndexError i wyświetl komunikat.

dane = [10, 20, 30]
try:
    print(dane[10])
except IndexError:
    print('Wybrales element z poza listy')

# 12.3 - Masz zmienną rabat z procentowym rabatem (np. rabat = 150). Jeśli rabat jest mniejszy niż 0 lub większy niż 100,
# rzuć ValueError z odpowiednim komunikatem. Przechwyć
# wyjątek za pomocą except ValueError as e i wypisz osobno typ błędu (type(e).__name__) oraz jego treść (e).

rabat = 150
try:
    if rabat < 0:
        raise ValueError('Rabat nie moze byc ujemny')
    if rabat > 100:
        raise ValueError('Rabat nie moze byc wiekszy niz 100')
except ValueError as e:
    print(f'Typ bledu: {type(e).__name__}')
    print(f'Komunikat: {e}')
else:
    print(f'Rabat: {rabat}')


"""
while True:
    try:
        wiek = int(input('Podaj swoj wiek: '))
        if wiek < 0 or wiek > 150:
            print('Wiek musi byc miedzy 0 a 150!')
            continue
        break
    except ValueError:
        print(f'To nie jest liczba! Sprobuj ponownie')


print(f'Twoj wiek: {wiek}')
"""

# hierarchi

# BaseException
#   ├── KeyboardInterrupt   (Ctrl + C)
#   ├── SystemExit          (exit())
#   └── Exception
#         ├── ValueError
#         ├── TypeError
#         ├── AttributeError
#         ├── ArithmeticError
#         │     └── ZeroDivisionError
#         ├── LookupError
#         │     ├── IndexError
#         │     └── KeyError
#         ├── OSError
#         │     └── FileNotFoundError
#         ├── RuntimeError
#         └── ... (i wiele innych)


# Exception lapanie - lapie prawie wszystko (ale nie KeyboardInterrupt i SystemExit)
try:
    int('abd')
except Exception as e:
    print(f'Zlapano: {type(e).__name__}: {e}')

# Uwaga: nie lapiemy BaseException, bo zlapie tez Ctrl + C (KeyboardInterrupt) i exit() (SystemExit)
# i programu nie da sie normalnie przerwac ani zamknac


# ============================================================
# 13. Funkcje
# ============================================================


# przywitaj_sie_z_widzami() # NameError: name 'przywitaj_sie_z_widzami' is not defined

def przywitaj_sie_z_widzami():
    print('Czesc!')

przywitaj_sie_z_widzami() # Czesc!
przywitaj_sie_z_widzami() # Czesc!
przywitaj_sie_z_widzami() # Czesc!

def przywitaj_sie_z_widzami():
    print('Witaj!')

przywitaj_sie_z_widzami() # Witaj!
przywitaj_sie_z_widzami() # Witaj!
przywitaj_sie_z_widzami() # Witaj!

przywitaj = przywitaj_sie_z_widzami() # Witaj!

print(przywitaj) # None
# przywitaj() # TypeError: 'NoneType' object is not callable

# Zwracanie wynikow funkcji
# return
def oblicz_sume():
    wynik = 5 + 3
    return wynik

wynik = oblicz_sume()
print(wynik)            # 8
print(oblicz_sume())    # 8

def oblicz():
    return 5 + 3
    print('tego nie zobaczysz')

oblicz()

# zwracanie wynikow przez return w wiekszej ilosci
def policz_min_max():
    lista = [1,2,3,8,5,8,5,7,3]
    return min(lista), max(lista)

wynik = policz_min_max()
print(wynik)                # (1, 8) # automatycznie pakuje w krotke

mi, ma = policz_min_max()
print(mi,ma)                # 1 8

# zaleznosc funkcji wbudowane zmienne

def policz():
    sumowanie = [2,8,4,5]
    return sum(sumowanie)

print(policz())
# Zmienna w funkcji jest niewidoczna na zewnatrz i nie da sie do niej odniesc
# print(sumowanie) # NameError: name 'sumowanie' is not defined

# 13.1 - Napisz funkcję powitanie(), która pyta użytkownika o imię (input())
# i wyświetla Cześć [imie]!. Wywołaj ją 3 razy.

"""
def powitanie():
    imie = input('Podaj imie: ')
    print(f'Czesc {imie}!')
powitanie()
powitanie()
powitanie()
"""

# 13.2 - Napisz funkcję linia_separatora(), która wypisuje linię
# złożoną z 30 znaków = (wykorzystaj mnożenie stringa: "=" * 30).

def linia_separatora():
    print('='*30)
linia_separatora()

# 13.3 - Napisz funkcję oblicz_iloczyn(), która oblicza iloczyn liczb 4 i 7 i
# zwraca wynik (bez parametrów - liczby na sztywno w środku funkcji).

def oblicz_iloczyn():
    return 4 * 7
wynik = oblicz_iloczyn()
print(wynik)

# 13.4 - Napisz dwie funkcje: podziel_print(), która wypisuje wynik dzielenia 10 / 3, oraz podziel_return(),
# która ten sam wynik zwraca. Przypisz wynik wywołania obu funkcji do zmiennych i wypisz te zmienne - zaobserwuj różnicę.

def podziel_print():
    print(10/3)

def podziel_return():
    return 10/3

print('\npodziel_print:')
t = podziel_print()
print(t)
print('\npodziel_return:')
w = podziel_return()
print(w)

"""
def sprawdz_haslo():
    haslo = input('Podaj haslo: ')
    if haslo == "1234":
        return "Haslo poprawne"
    return 'Haslo niepoprawne'

print(sprawdz_haslo())
"""

"""
def sprawdz_wiek():
    wiek = int(input("Podaj wiek: "))
    if wiek < 0:
        return 'Blad wiek ujemny'
    if wiek < 18:
        return 'Niepelnoletni'
    return 'Pelnoletni'

print(sprawdz_wiek())
"""

# 13.5 - Napisz funkcję sprawdz_liczbe(),
# która pyta użytkownika o liczbę i zwraca "Dodatnia", "Ujemna" lub "Zero",
# w zależności od wartości.

"""
def sprawdz_liczbe(l): # nazwa l odradzana w PEP 8, latwo pomylic z 1 i I
    if l >0:
        return "Dodatnia"
    elif l<0:
        return "Ujemna"
    return "Zero"

print(sprawdz_liczbe(int(input('Wprowadz liczbe: '))))
"""

# drugie rozwiazanie, zgodnie z trescia: funkcja sama pyta uzytkownika o liczbe
"""
def sprawdz_liczbe():
    liczba = int(input('Podaj liczbe: '))
    if liczba > 0:
        return "Dodatnia"
    if liczba < 0:
        return "Ujemna"
    return "Zero"

print(sprawdz_liczbe())
"""

# 13.6 - Napisz funkcję sprawdz_ocene(), która pyta użytkownika o ocenę (1-6) i
# - używając wczesnego return - zwraca "Zaliczone", jeśli ocena jest równa co najmniej 3,
# w przeciwnym razie "Niezaliczone".

"""
def sprawdz_ocene():
    if int(input("Podaj ocenę w skali od 1 do 6: ")) >= 3:
        return "Zaliczone"
    return "Niezaliczone"

print(sprawdz_ocene())
"""

# Parametry funkcji
def przywitaj(imie):
    print(f'Czesc! {imie}')

przywitaj('Adam')
przywitaj('Ola')

# wiele parametrow w jednym miejscu
def dodaj(a,b):
    print(f'{a} + {b} = {a+b}')

dodaj(3,5)
dodaj(6,4)

# ile mamy przekazywanych argumentow
# dodaj(3,5,6)       # TypeError: dodaj() takes 2 positional arguments but 3 were given
# dodaj(3,5,6,6,7,5) # TypeError: dodaj() takes 2 positional arguments but 6 were given
# dodaj(1)           # TypeError: dodaj() missing 1 required positional argument: 'b'

# Wartości domyślne parametrów

def przywitaj(imie,powitaj='Czesc'):
    print(f'{powitaj} {imie}!')

przywitaj("Adam")           # Czesc Adam!
przywitaj("Adam", "Hej")    # Hej Adam!
przywitaj("Adam", "Witaj")  # Witaj Adam!

# Pulapki

# Parametry z wartoscia domyslna ZAWSZE NA KONCU!

# def przywitaj(powitaj='Czesc',imie): # SyntaxError: parameter without a default follows parameter with a default
#     print(f'{powitaj} {imie}!')

# mutowalnosc
def dodaj_do_listy(element, lista=[]):
    lista.append(element)
    return lista

print(dodaj_do_listy("a")) # ['a']
print(dodaj_do_listy("b")) # ['a', 'b'] --> na logike powinno byc tylko ['b']!


def dodaj_do_listy(element, lista=None):
    if lista is None:
        lista = []
    lista.append(element)
    return lista

print(dodaj_do_listy("a")) # ['a']
print(dodaj_do_listy("b")) # ['b']

# 13.7 - Napisz funkcję pole_prostokata(a, b), która zwraca (return) pole prostokąta. Wyświetl wynik.

def pole_prostokata(a,b):
    return a*b
print(f'Wynik: {pole_prostokata(4,5)}')

# 13.8 - Napisz funkcję maks(a, b, c), która zwraca największą z trzech liczb. To ćwiczenie na parametry
# - możesz spokojnie skorzystać z wbudowanej max().

def maks(a, b, c):
    return max(a, b, c)

print(maks(4, 2,5))

# 13.9 - Napisz funkcję odwroc(tekst), która zwraca odwrócony string. Np. "Python" → "nohtyP".

def odwroc(tekst):
    return tekst[::-1]
# Uwaga: w Pythonie starszym niz 3.12 te same apostrofy wewnatrz f-stringa daja SyntaxError i nie uruchomi sie caly plik
print(f'{odwroc('Wroclaw')}') # walcorW # te same '' w srodku f-stringa dzialaja od pythona 3.12, nizej SyntaxError --> f'{odwroc("Wroclaw")}'

# 13.10 - Napisz funkcje potega z domyslnym wykladnikiem 2 --> potega(5) → 25, potega(2, 10) → 1024.

def potega(podstawa, wykladnik=2):
    return podstawa**wykladnik
print(potega(5))
print(potega(2,10))

# Dokumentacja funkcji - docstring

def pole_kola(r):
    """Oblicza pole kola na podstawie promienia r."""
    # docstringi zawsze umieszczamy na gorze pod nazwa funkcji
    return 3.14 * r **2


# odczytywanie dokumentacji
# help(pole_kola) # uzyteczne dla wiekszych dokumentacji
print(pole_kola.__doc__) # Oblicza pole kola na podstawie promienia r.


def oblicz_bmi(waga,wzrost):
    """
    Oblicza wskaznik BMI

    Args:
        waga: Waga w kilogramach (float)
        wzrost: Wzrost w metrach (float)

    Returns:
        Wartosc BMI zaokraglona do 1 miejsca po przecinku (float)

    Raises:
        ValueError: Jesli waga lub wzrost <= 0
    """
    if waga <= 0 or wzrost <= 0:
        raise ValueError('Waga i wzrost musza byc wieksze od 0!')
    return round(waga / wzrost **2,1)

print(oblicz_bmi(75,1.80)) # 23.1
# help(oblicz_bmi) q --> kliknij q zeby zamknac
# print(oblicz_bmi.__doc__)


# type hint --> podpowiedz jaki typ powinien wejsc do funkcji
# python tego nie pilnuje, funkcja(75) i funkcja('abc') przejda tak samo, podpowiada tylko edytor
def funkcja(waga: float):
    pass

# *args **kwargs

# args - dowolna ilosc argumentow pozycyjnych *reszty --> *args

def suma(*args):
    print(f'Argumenty: {args}') # (1, 2, 3)
    return sum(args)

print(suma(1,2,3))          # 6
print(suma(5,10,15,20))     # 50

def pokaz_args(*args):
    print(args)
    print(*args)

print(pokaz_args(1,2,3)) # (1, 2, 3) --> 1 2 3 --> None (funkcja bez return)


# **kwargs -> zbiera argumenty nazwane (klucz=wartosc)

def wyswietl_dane(**kwargs):
    for klucz, wartosc in kwargs.items():
        print(f'{klucz}: {wartosc}')

wyswietl_dane(imie='Adam',wiek=28,miasto='krakow')

# imie: Adam
# wiek: 28
# miasto: krakow

# Poprawne umeiszczenie / kolejnosc parametrow z *args i **kwargs
# def dane_do(imie,dominic,*args,**kwargs,dominik='dominik'): # SyntaxError: arguments cannot follow var-keyword argument
# def dane_do(dominik='dominik',imie,dominic,*args,**kwargs): # SyntaxError: parameter without a default follows parameter with a default
def dane_do(imie,dominic,*args,dominik='dominik',**kwargs):
    print(1, imie)
    print(2, dominic)
    print(3, dominik)
    print(4, args)
    print(5, kwargs)

dane_do('adam','ja',3,4,5,6,43,rozrzutnik='abc',lata='dwaczy')


# 13.11 - Napisz funkcję srednia(*args), która przyjmuje dowolną liczbę liczb i zwraca ich średnią.
# Dodaj rozbudowany docstring z Args i Returns.

def srednia(*args):
    """
    Oblicza srednia z podanych liczb

    Args:
        *args: Dowolna ilosc liczb (int lub float)

    Returns:
        Sredna arytmetyczna (float)

    """
    suma = 0
    for liczba in args:
        suma += liczba
    return suma / len(args)

print(srednia(5,10,15)) #10.0
print(srednia.__doc__)

# 13.12 - Napisz funkcję najwieksza(*args), która zwraca największą z podanych liczb (dowolna ich ilość).
# Nie martw się o docstring - skup się na samym *args.

def najwieksza(*args):
    return max(args)

print(najwieksza(22,7,56,45,76.9)) # 76.9