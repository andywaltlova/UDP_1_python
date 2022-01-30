import statistics
kocicky = ['mourek', 'pruhovana', 'cerna']

# for kocicka in kocicky:
#     print(kocicka.lower())


znamky = [1, 2, 3, 3, 3, 0]
soucet = 0
for cislo in znamky:
    # soucet += cislo
    soucet = soucet + cislo

prumer = statistics.mean(znamky)

print(f"Prumer znamek je: {prumer}")
print(soucet)
print(sum(znamky))
