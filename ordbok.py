

# Steg 2 
def vis_alle():
    if len(telefonbok) == 0:
        print("Telefonboka er tom.")
    else:
        for person in telefonbok:
            print(f'{person["navn"]}: {person["nummer"]}')

