import random
import math

# 1 Délka názvu
# Uložte si do proměnné nazev řetězec s názvem “Divadlo Pěst na oko”. Pokud použijeme designové písmo nad hlavní vchod budovy, jeden znak(i mezera) bude široký 30 cm. Použijte funkci len() abyste zjistili počet znaků v názvu divadla a spočítejte délku nápisu v centimetrech.
nazev = "Divadlo Pěst na oko"
delka = len(nazev) * 30

# 2 Zaokrouhlování
# Divadlo chce mít ceny vstupenek jak v eurech tak v celých korunách. Uložte do proměnné eura cenu studentské vstupenky(65 % z 12 euro). Použijte funkci round() a do proměnné koruny spočítejte kolik činí studentské vstupné v korunách jestliže kurz eura je 24 korun.
cena = 12 * 0.65
koruny = round(24 * cena)

# 3 Zaokrouhlování nahoru
# Importujte modul math a vyzkoušejte si funkci math.ceil(), která slouží k zaokrouhlování směrem nahoru. Proveďte zaokrouhlování z předchozího cvičení na celé koruny směrem nahoru.
koruny = math.ceil(24 * cena)

# 4 Náhodná čísla
# Na informačním panelu v předsálí divadla se zobrazují informace o náhodných představeních. Pro tento panel potřebujeme generátor náhodných čísel, který bude generovat čísla představení mezi 1 až 24. Importujte modul random a použijte funkci randint() pro vygenerování několika náhodných čísel z tohoto rozsahu.
cislo = random.randint(1, 24)

# Bonusy

# 5 Klasické zaokrouhlování
# Překvapivě Python neobsahuje žádnou funkci, která by dělala klasické zaokrouhlování, tedy takové, na které jsme všichni zvyklí ze školy. S něčím takovým se nemůžeme spokojit.
# Zkuste vymyslet(za použití funkcí, které už znáte) příkaz, který zaokrouhlí číslo v proměnné cislo na celé číslo klasickým zaokrouhlováním.
cislo = 2.5
zaokrouhlene = math.floor(cislo + 0.5)

# Pokud si chcete svoje řešení otestovat, můžete si obsah proměnné cislo vygenerovat náhodně funkcí random.uniform(). Ta má stejné vstupy jako funkce random.randint(), generuje ale desetinná čísla.
cislo = random.uniform(0, 10)
zaokrouhlene = math.floor(cislo + 0.5)