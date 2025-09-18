# Oppgave 4 
def sok():
    navn_sok = input("Skriv inn navnet du vil søke etter: ")
    funnet = False
    for person in telefonbok:
        if person["navn"].lower() == navn_sok.lower():
            print(f'{person["navn"]}: {person["nummer"]}')
            funnet = True
    if not funnet:
        print("Fant ingen med det navnet.")
