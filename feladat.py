"""
2-3 fős csoportokban készítsetek egy lottó játékot!
Legyen lehetőség a játékos tippjeinek a felvételére!
Utána a program sorsoljon ki számokat!
Végül írjuk ki, hogy mennyi találat volt!
Ha tudjátok, többféle lottó játékkal is lehessen játszani!
"""
jatekos_szamok = []

jatekos_szamok.sort()

ujra = 5
while ujra > 0:
    megadott_szamok = int(input("Adj meg egy számot:"))
    ujra -= 1
    jatekos_szamok.append(megadott_szamok)


print(jatekos_szamok)

import random

random_szamok = [random.randint(0,90) for _ in range(5)]

random_szamok.sort()

print (random_szamok)

jatekos_szamok_set= set(jatekos_szamok)

def eltalalt_szamok(jatekos_szamok_set, random_szamok):
    return len(jatekos_szamok_set.intersection(random_szamok))


eltalalt = eltalalt_szamok(jatekos_szamok_set, random_szamok)
print (f"sikeres találatok: {eltalalt}")


if eltalalt == 0:
   print("greater skill issue")

elif eltalalt == 1:
    print("skill issue")

elif eltalalt == 2:
    print("lesser skill issue")

elif eltalalt == 3:
    print("GAMBLING YEAAAAAAHHHHHHHHHHH!!!!!!!!!!!!!")

elif eltalalt == 4:
    print("menjé lottózni")

elif eltalalt == 5:
    print("touch grass")