# 1 Jednoduchý výstup
# Náš vůbec první program nebude dělat nic víc, než vypisovat text na obrazovku.

# Založte si program vstup-vystup.py. V tomto programu pomocí funkce print() vypište na obrazovku Divadlo Pěst na oko. Program spusťte na konzoli a vyzkoušejte, že dělá co má.
# Upravte tento program tak, že do proměnné nazev uložíte název nějakého divadelního představení a do proměnné cas uložte čas konání tohoto představení. Nyní pomocí funkce print() nechte program vypsat na obrazovku na jeden řádek název představení a čas konání, např. Zkrocení zlé ženy - 19: 30.
# Upravte dále program tak, že do proměnné hodina uložíte hodinu konání představení(jako celé číslo) a do proměnné minuta minutu konání, také jako celé číslo. Zařiďte, aby výstup programu vypadal takto: Zkrocení zlé ženy - 19: 30. Pozor na to, že hodina a minuta je hodnota typu číslo, takže ji budete při výpisu muset převést na řetězec pomocí funkce str().

# 2 Jednoduchý vstup
# Teď už budeme chtít, aby náš program dokázal získat vstup od uživatele.

# Napište program jmeno.py, který získá jméno a příjmení od uživatele voláním funkce input(). Vypište je na obrazovku podobně jako v předchozím cvičení.
# Nechte uživatele zadat také věk. Pozor na to, že funkce input() vždy vrací řetězec, ale my chceme v proměnné vek mít číslo. Použijte tedy funkci int(), abyste převedli uživatelem zadaný řetězec na číslo. Opět vypište na obrazovku jméno, příjmení a věk tak jako v předchozí verzi.

# 3 Zakázka pro divadlo
# Divadlo požaduje systém pro online rezervaci vstupenek na pořádaná představení. Váš první úkol na této zakázce je vytvořit registraci pro nové uživatele tohoto systému.

# Založte si program vstupenky01.py. Bude to první verze našeho programu pro nákup vstupenek.
# Napište program tak, aby nejprve vypsal na obrazovku Divadlo Pěst na oko na první řádek, na druhý řádek chceme vypsat Vítejte v online rezervaci vstupenek a na třetí řádek Pro vstup do systému je potřeba registrace.
# Na dalším řádku požádejte uživatele o jeho uživatelské jméno a poté o jeho věk. Ten si uložte to nějaké proměnné jako číslo.

# Bonusy

# 4 Házení kostkami
# Napište program kostky.py, který bude simulovat hod dvěma klasickými šestistěnnými kostkami. Jeho výstupu bude součet bodů na těchto dvou kostkách.

# Nápověda:

# Generování náhodných čísel dělá funkce random.randint().
# Pokud chcete ve vašem programu použít modul random, musíte na jeho úplném začátku napsat příkaz

# 5 Generátor čísel
# Napište program generator.py, který si od uživatele vyžádá dvě celá čísla - dolní mez a horní mez - a vypíše na výstup náhodné číslo v zadaných mezích.
