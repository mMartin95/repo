
"""
projekt_1_Rihacek.py: první projekt do Engeto Online Python Akademie

author: Martin Řiháček
email: martinrihacek@seznam.cz
discord: mMartin95

""" 
#Přiložený text, je to list!!!

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#1.) Nastavení hodnot pro zpracování projektu

slovnik_jmen_hesel = {"bob":"123", "ann":"pass123", "mike":"password123", "lizz":"pass123"} 
oddelovac1 = "_" * 65


#2.) Vložení uživatelského jména a hesla

username = input("Zadejte vaše uživatelské jméno: ")
password = input("Zadejte vaše heslo: ")

print("username: " + username)
print("password: " + password)

#3.) Vytvoření podmínky pro ověření uživatelského jména a hesla


if username in slovnik_jmen_hesel and password == slovnik_jmen_hesel[username]:
    print(oddelovac1, end = "\n")
    print(f"Ahoj {username}, vítej v naší aplikaci\n")
    print("Máme pro tebe na výběr 3 soubory textů, které musí být analyzovány\n")
    print(oddelovac1, end = "\n")
else:
    print("Neregistrovaný uživatel, dochází k vypnutí programu..")
    quit()

#4.) Práce se souborem TEXTS a výběr čísla


cislo_TEXTS = int(input("Vyber si číslo od 1 do 3: ")) - 1

vybrany_text = TEXTS[cislo_TEXTS] 

#Pocítalo mi to 316 slov (včetně mezer), proto jsem si musel text upravit pomocí metody split

upraveny_TEXTS = vybrany_text.split()

pocet_slov = len(upraveny_TEXTS)
pocet_titlecase = sum(1 for slovo in upraveny_TEXTS if slovo and slovo[0].isupper())
pocet_upper = sum(1 for slovo in upraveny_TEXTS if slovo.isupper() and not any(cislo.isdigit() for cislo in slovo))
pocet_lower = sum(1 for slovo in upraveny_TEXTS if slovo.islower())
pocet_cisel = sum(1 for slovo in upraveny_TEXTS if slovo.isdigit())

#Definovat čílo
cisla = [int(slovo) for slovo in upraveny_TEXTS if slovo.isdigit()]
suma_cisel = sum(cisla)

if cislo_TEXTS in range(3):
    print(f"Zde je {pocet_slov} slov ve zvoleném textu")
    print(f"Zde je {pocet_titlecase} slov s velkým počátečním písmenem")
    print(f"Zde je {pocet_upper} slov psaných velkými písmeny")
    print(f"Zde je {pocet_lower} slov psaných malými písmeny")
    print(f"Zde je {pocet_cisel} čísel v textu")
    print(f"Zde je součet čísel v textu: {suma_cisel} ")
else:
    print("Zvolené číslo není v rozsahu, proto dochází k ukončení programu ")
    quit()

print(oddelovac1)

#5.) Vytvoření sloupcového grafu ze slov s různou četností písmen
#Začátek grafu
print("LEN|  OCCURENCES  |NR.")
print(oddelovac1)

# Vytvoření slovníku pro uložení četnosti délek slov
délky_slov = {}

upraveny_TEXTS2 = []

#Odstranění znamének, jinak to háže jinou četnost
for slovo in upraveny_TEXTS:
    slovo = slovo.strip(".,:;!?_")
    upraveny_TEXTS2.append(slovo)


# Procházení slov v textu a zjištění délek slov
for slovo in upraveny_TEXTS2:
    délka = len(slovo)
    if délka not in délky_slov:
        délky_slov[délka] = 1
    else:
        délky_slov[délka] += 1


# Seřazení slovníku podle délky slov
seřazené_délky_slov = dict(sorted(délky_slov.items()))

# Sloupcový graf

for délka, četnost in seřazené_délky_slov.items():
    print(f"{délka:2}|{'*' * četnost:13}|{četnost:2}")


