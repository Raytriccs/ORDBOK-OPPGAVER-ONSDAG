# Oppgave 3 
def legg_til():
    navn = input("Skriv inn navn: ")
    nummer = input("Skriv inn nummer: ")
    ny_person = {"navn": navn, "nummer": nummer}
    telefonbok.append(ny_person)
    print(f"{navn} ble lagt til i telefonboka.")
