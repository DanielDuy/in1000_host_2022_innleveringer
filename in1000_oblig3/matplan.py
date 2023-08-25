# Oppgave 1
beboere = {
    "Kari Nordmann": ["brød", "egg", "pølser"],
    "Olda Svine": ["havregrøt", "panini", "taco"],
    "Per Olsen": ["frokostblanding", "suppe", "lasagne"],
}

for key in beboere: # For løkke som går gjennom alle nøkkelverdier i dict. ovenfor
    print(key)  # printer ut nøkkelverdi

# Oppgave 2
def print_maltid_beboer():  # Funksjon
    input1 = input('Skriv navnet til en beboer: ')  # Får input og lagrer i en variabel
    fant_beboer = False
    for key in beboere: # Går gjennom alle nøkkelverdier i dictionary-en
        if key == input1:   # Hvis input er lik en av navnene i dictionary-en
            print(beboere[input1])  # Printer ut måltidene/innholdserdien
            fant_beboer = True  # Gjør om variabelen til True
            break   # Stopper for-løkken
    if not fant_beboer: # Hvis beboeren ikke ble funnet, er variabelen 'False', og koden under kjøres
        print('Beboeren er ikke registrert, prøv igjen') # Printer ut melding
        print_maltid_beboer()   # Kjører funksjonen igjen

print_maltid_beboer()   # Kjører funksjonen for første gang

# Oppgave 3
# a.    Set, kun unike verdier, kan ikke endres
# b.    Dictionary, flere variabler
# c.    Liste, tillater samme navn
# d.    Set, unike verdier, kan legge til og fjerne variabler
