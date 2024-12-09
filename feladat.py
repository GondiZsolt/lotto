"""
2-3 fős csoportokban készítsetek egy lottó játékot!
Legyen lehetőség a játékos tippjeinek a felvételére!
Utána a program sorsoljon ki számokat!
Végül írjuk ki, hogy mennyi találat volt!
Ha tudjátok, többféle lottó játékkal is lehessen játszani!
"""
jatekos_szamok = []

ujra = 5
while ujra > 0:
    megadott_szamok = int(input("Adj meg egy számot:"))
    ujra -= 1
    jatekos_szamok.append(megadott_szamok)

print(jatekos_szamok)

import random

random_szamok = [random.randint(0,90) for _ in range(5)]

print (random_szamok)

def eltalalt_szamok(jatekos_szamok, random_szamok):
    return len(jatekos_szamok.intersection(random_szamok))

eltalalt
