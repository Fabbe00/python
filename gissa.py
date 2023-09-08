# Denna uppgift ska vi öva variabler vilkor och loopar
import random
import os
os.system("cls"if os.name == "nt" else "clear")
print("\m---------------------------")
print(".Gissa.")


print("gissa ett tal mellan 1 och 10 pröva lyckan, du får tre försök!\n")
slumptal = random.randint(1, 10)
#print(slumptal)

i=0
hitta = False

#looper

while i < 3:

    gissatal = input(" mata in tal.")
    if slumptal == int(gissatal):
        hitta = True
        print("\n Rätt svar!")
        break
    i += 1
    
    if slumptal < int(gissatal):
        print("\n Gissa lägre")

    else:
        if i == 3:
            break
        else:
            print("\n Gissa högre")    

    if i == 1:
        print("\n Två försök kvar")

    if i == 2:
        print("\n Ett försök kvar!")    

if hitta: 
    print("\n Bra jobbat, ditt pris är:")
    list = [" En anka", 
            " Mark i Sibirien", 
            " En biljett till den sämsta filmen du nånsin kommer att se", 
            " Tillgång till Amins tankar",
            " Lyssna på allt Alloush har att säga",
            " Bli skyldig så mycket pengar att Lyxfällan gör en hel säsong bara om dig",
            " En halv påse badsalt",
            " En extra Alloush",
            " Ingenting"
            ]
    rand_num = random.choice(list)
    print(rand_num)

else:
    print("\n Ditt svar var fel, bättre lycka nästa gång")

print("\n------------------------------------------------------------")