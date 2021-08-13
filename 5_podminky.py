# 1 Jednoduché podmínky
# Založte si program prihlaseni.py. V tomto nechte uživatele zadat svoje uživatelské jméno a poté heslo. Pokud se heslo shoduje s heslem simsalabim vypište na výstup
# Smíš vstoupit
# Program spusťte na konzoli a vyzkoušejte, že dělá co má.
# Upravte tento program tak, aby vypsal
# Vstup nepovolen
# pokud uživatel zadá špatné heslo.

# Upravte dále program tak, že pokud uživatel zadá správné heslo, program se ho ještě zeptá na věk a pustí jej dál pouze pokud je starší 18ti let. Pokud uživatel zadá heslo špatně, už se ho na věk neptejte a ukončete program voláním funkce exit().
uzivatel = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")
if heslo == "simsalabim":
    vek = input("Zadej věk: ")
    vek = int(vek)
    if vek > 18:
        print("Smíš vstoupit.")
else:
    print("Vstup nepovolen!")
    exit()

# 2 Cena vstupenky
# A nyní opět pokračujeme v našem rezervačním systému.

# Program vstupenky01.py, který jste napsali v předchozí fázi, si uložte jako vstupenky02.py, abychom ho mohli dále rozšířit o výpočet ceny vstupenky.
# Jakmile máte v programu načtený věk uživatele, vytvořte si proměnnou plna_cena, do které uložte hodnotu 12.
# Vytvořte podmínku, která do proměnné cena uloží cenu spočítanou podle věku uživatele dle následujících pravidel
# 0 euro pro návštěvníky mladší 6 let,
# 65 % ze základní ceny pro návštěvníky 6 až 26 let(žák, student),
# 100 % ze základní ceny pro návštěvníky 27 až 64 let(dospělý),
# 50 % ze základní ceny pro ostatní(senior).
# Nezapomeňte na zaokrouhlování, ať nám cena vyjde v celých centech.
# Nakonec spočtenou cenu vypište s nějakou hezkou zprávou na výstup.
print("Divadlo Pěst na oko")
print("Vítejte v online rezervaci vstupenek")
print("Pro vstup do systému je potřeba registrace")
uzivatel = input("Zadej uživatelské jméno: ")
vek = input("Zadej věk: ")
vek = int(vek)
plna_cena = 12
if vek < 6:
    cena = 0
elif vek <= 26:
    cena = plna_cena * (1 - 0.65)
elif vek <= 64:
    cena = plna_cena
else:
    cena = plna_cena * 0.5
cena = round(cena, 2)
print(f"Cena vstupenky je {cena}.")
print("Cena vstupenky je " + str(cena) + ".")


# Bonusy

# 3 Registrace
# Založte si program registrace.py. Program nechá uživatele, aby si zvolil uživatelské jméno a heslo. Heslo jej nechejte zadat dvakrát a ověřte, že jej uživatel zadal dvakrát stejně. V opačném případě vypište varování, že hesla nejsou stejná. Při prvním zadávání ověřte, že heslo je bezpečné, což v tomto případě znamená, že je delší než 8 znaků.
uzivatel = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")
heslo2 = input("Zadej heslo znovu: ")
if heslo != heslo2:
    print("Hesla se neshodují.")
elif len(heslo) <= 8:
    print("Heslo je příliš krátké")

# 4 Ruleta
# Na obrázku vidíte rozložení čísel na klasické Francouzské ruletě. Ruleta obsahuje čísla 0 - 36. Každé číslo s výjimkou nuly je buď sudé nebo liché a zároveň červené nebo černé. Pro čísla 1 až 10 a 19 až 28 platí, že lichá čísla jsou červená a sudá jsou černá. Pro zbytek platí obrácené pravidlo, tedy lichá jsou černá a sudá červená. Nula není ani lichá ani sudá, ani černá ani červená.
# Napište program, kterému uživatel zadá číslo a program odpoví jestli jde o číslo sudé nebo liché, černé nebo červené, nebo je to nula.

"""
Klíčová slova and a or jsou popsaná zde: 
http://nove.kodim.cz/czechitas/progr2-python/zaklady-programovani-2/podminky-2
"""

cislo = input("Zadej čislo: ")
cislo = int(cislo)

if cislo == 0:
    print("Číslo je 0.")
else:
    if cislo % 2 == 0:
        print("Číslo je sudé.")
    else:
        print("Číslo je liché.")
    if cislo <= 10 or (cislo >= 19 and cislo <= 28):
        if cislo % 2 == 0:
            print("Číslo je černé.")
        else:
            print("Číslo je červené.")
    else:
        if cislo % 2 == 1:
            print("Číslo je černé.")
        else:
            print("Číslo je červené.")

# 5 Přestupný rok
# Napište program, který po zadání kalendářního roku vypíše, zda jde o rok přestupný, či nikoliv. Letopočet je přestupný, pokud je dělitelný čtyřmi. Roky, které jsou dělitelné 100 jsou ovšem přestupné pouze tehdy, jsou-li zároveň dělitelné 400.

rok = input("Zadej rok: ")
rok = int(rok)
if rok % 4 == 0:
    if rok % 100 == 0:
        if rok % 400 == 0:
            print("Rok je přestupný.")
        else:
            print("Rok není přestupný")
    else:
        print("Rok je přestupný.")
else:
    print("Rok není přestupný.")

"""
Alternativní řešení pomocí klíčových slov and a or.
Klíčová slova and a or jsou popsaná zde: 
http://nove.kodim.cz/czechitas/progr2-python/zaklady-programovani-2/podminky-2
"""

if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
    print("Rok je přestupný.")
else:
    print("Rok není přestupný")
