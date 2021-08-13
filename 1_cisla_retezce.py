# 1 Jednoduchá aritmetika
# Použijte Python konzoli jako kalkulačku:
# Jeden lístek do divadla “Pěst na oko” stojí 12 euro. Spočítejte měsíční příjem divadla ze vstupného přichází-li průměrně 174 návštěvníků na jedno představení a divadlo hraje 15 představení měsíčně.
12 * 174 * 15

# Divadlo se rozhodlo prodávat studentské vstupné ve výši 65% plného vstupného. Jak se změní měsíční příjem divadla pokud víme, že polovina návštěvníků jsou studenti?
12 * 174 / 2 * 15 + 12 * 174 / 2 * 15 * 0.65
12 * 15 * 174 / 2 * (1 + 0.65)

# 2 Hrátky s řetězci
# Vytvořte řetězec obsahující jméno divadla.
"Divadlo Pěst na oko"
# Vytvořte řetězec obsahující jméno divadla tak, že sečtete dohromady jednotlivá slova toho jména.
"Divadlo " + "Pěst " + "na " + "oko"
# Zkuste vynásobit řetězec celým číslem. Jaký jste dostali výsledek?
"Divadlo Pěst na oko " * 5
# Vytvořte řetězec který vypadá takto: ‘111111000000’, ale místo šesti jedniček a šesti nul obsahuje 256 jedniček a 256 nul.
"1" * 256 + "0" * 256

# Bonusy

# 3 Úroky
# Fíha banka a.s. nabízí na svých stránkách spořící účet s úrokem 2, 4 % . Když si na takový účet uložíte 1 000 000 kč, kolik peněz nastřádáte za 10 let?
1000000 * (1 + 0.024) ** 10

# 4 Nový koberec
# Do malého sálu v divadle, který má tvar čtverce o rozloze 30 m2 potřebujeme koupit nový koberec. Jakou délku má mít strana koberce? Vejde se nám srolovaný do dodávky s nákladovým prostorem dlouhým 5 m?
30 ** 0.5

# 5 Shannonovo číslo
# Takzvané Shannonovo číslo má hodnotu 10120 a udává kolik nejméně lze odehrát různých šachových partií. Vytvořte řetězec, který obsahuje toto číslo zapsané běžným způsobem pomocí cifer. Například 103 je 1000, 106 je 1000000 atd.
"1" + "0" * 120
# Čísla s mnoha nulami je v Česku zvykem zapisovat tak, že každé tři nuly následuje mezera. Jeden milión se tedy zapíše jako 1 000 000. Vytvořte řetězec, který obsahuje Shannonovo číslo z předchozího cvičení zapsané v tomto formátu.
"1" + "000 " * (120 // 3)
