# Oppgave 1, 2
teller = 0
while teller < 3:  # Ved hjelp av variabelen "teller", så kjører koden under 3 ganger
    teller += 1
    navn = input("Skriv inn navn: ")  # Input navn
    bosted = input("Hvor kommer du fra? ")  # Input sted
    print("Hei, {}! Du er fra {}. \n".format(navn, bosted))  # Printer ut variablene i en streng.
