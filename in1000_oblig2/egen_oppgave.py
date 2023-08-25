# Oppgave 5
# Lag en sjekkliste om gyldige inputs for å opprette en ny bruker.

bruker_brukernavn = ""
bruker_epost = ""
bruker_tlf = ""
bruker_passord = ""

gyldig_bruker_navn = False  # Endres til True ved hjelp av if-setning under
while not gyldig_bruker_navn:   # Loop som kjører programmet under hvis variabelen ovenfor ikke er True
    bruker_navn = input("Brukernavn: ") # input brukernavn
    if bruker_navn.isalnum():   # Sjekker om inputen inneholder kung "alphanumeric" tegn
        bruker_brukernavn = bruker_navn # Angir brukernavn til global variabelen
        gyldig_bruker_navn = True   # Endrer variabelen til True, og går ut av loopen
    else:
        print("Ugyldig brukernavn") # Hvis det er ugyldig brukernavn, printes dette

# Nesten alle loopene er det samme utenom små forskjell

gyldig_epost = False
while not gyldig_epost:
    epost = input("E-post adresse: ")
    bruker_epost = epost
    epost = epost.replace("@", "")  # Fjerner tegnet "@" fra variabelen
    epost = epost.replace(".", "")  # Fjerner tegnet "." fra variabelen
    if epost.isalnum(): # Sjekker om resten av tegnene i variabelen er alphanumeric
        gyldig_epost = True
    else:
        print("Ugyldig epost")

gyldig_tlf = False
while not gyldig_tlf:
    tlf = input("Telefonnummer: ")
    if tlf.isdigit():   # Sjekker om tegenene er kun tall
        bruker_tlf = tlf
        gyldig_tlf = True
    else:
        print("Ugyldig tlf")

gyldig_passord = False
while not gyldig_passord:
    passord = input("Passord: ")
    if passord.isalnum():
        gyldig_bekreft_passord = False
        while not gyldig_bekreft_passord:   # Enda en while loop for å bekrefte passord
            bekreft_passord = input("Bekreft passord: ")    # input for bekreft passord
            if bekreft_passord == passord:  # Hvis den andre passordet som ble skrevet inn er lik den første passordet
                bruker_passord = bekreft_passord    # Angi passordet til global variabelen
                gyldig_bekreft_passord = True   # Går ut av andre loopen
        gyldig_passord = True   # Går ut av første loopen
    else:
        print("Ugyldig eller ulike passord")

# Printer ut brukeren
print("\nBruker opprettet!\n")
print(bruker_brukernavn)
print(bruker_epost)
print(bruker_tlf)
print(bruker_passord)
