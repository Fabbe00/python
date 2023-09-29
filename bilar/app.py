import bil 

looping = True 

volvo_kalsong_blå = bil.Bil("Volvo", "Kalsong Blå", 3)
daf_gul = bil.Bil("Daf", "Gul", 1)
ford_galaxie_500_röd = bil.Bil("Ford Galaxie 500", "Röd", 1)
chevelle_ss_blå = bil.Bil("Chevelle SS", "Blå", 2)
ford_kcode_röd = bil.Bil("Ford K-Code", "Röd", 1)


billista = [ volvo_kalsong_blå, daf_gul, ford_galaxie_500_röd, chevelle_ss_blå, ford_kcode_röd]

while looping:
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print("\n\t -=BilAutomat:=-")

    i=0

    for bil in billista:
        print(f"{i+1} : {bil.fabrikat} : {bil.color} : Antal={bil.lager}")
        i = i + 1

    bil_nr = input("\nMata in siffra för vald bil") 

    bil_nr_int = int(bil_nr)

    lager_int = billista[bil_nr_int-1].getLager()
    lager_string = str(lager_int)

    if lager_int > 0:
        print(f"\n En {billista[bil_nr_int-1].color}{billista[bil_nr_int-1].fabrikat} kommer här!")

        #Minskar lager saldo

        nytt_lagersaldo_int = lager_int - 1
        nytt_lagersaldo_str = int(nytt_lagersaldo_int)

        billista[bil_nr_int-1].setlager(nytt_lagersaldo_int)

    else :
        print(f"Tyvärr slut på biltypen {billista[bil_nr_int-1].fabrikat}")

    print(f"Lager saldo före: {lager_string}")
    print(f"Lager saldo efter: {nytt_lagersaldo_str}")
    print("-------------------------")


    go = input("Vill du avsluta programmet y/n")

    if (go == "y"):
        break