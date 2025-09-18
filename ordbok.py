# Oppgave 5 
def hovedmeny():
    while True:
        print("\nMeny:")
        print("1. Vis alle")
        print("2. Legg til ny")
        print("3. Søk")
        print("4. Avslutt")
        valg = input("Velg et tall: ")

        if valg == "1":
            vis_alle()
        elif valg == "2":
            legg_til()
        elif valg == "3":
            sok()
        elif valg == "4":
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg, prøv igjen.")

