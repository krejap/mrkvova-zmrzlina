from pojisteny import Pojisteny

evidence = []
pokracovat = "ano"

while pokracovat == "ano":
    print("Vyberte jednu z požadovaných operací: ")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")        
    moznost = int(input(" "))

    if (moznost == 1):        
        print("Přidat nového pojištěného\n")
        jmeno = input("Zadejte jméno: \n")
        prijmeni = input("Zadejte příjmení: \n")
        vek = int(input("Zadejte věk: \n"))
        tel_cislo = input("Zadejte telefonní číslo: \n")
        novy_pojisteny = Pojisteny(jmeno, prijmeni, vek, tel_cislo)
        print(novy_pojisteny)
        evidence.append(novy_pojisteny)
        print("Data byla uložena. Pokračujte libovolnou klávesou\n")

    elif (moznost == 2):
        for i in evidence:
            print(i)

    elif (moznost == 3):
        zadany_pojisteny = input("Zadej pojisteneho: \n")
        for i in evidence:
            if (i.prijmeni == zadany_pojisteny):
                print(i)

    else:
        break
