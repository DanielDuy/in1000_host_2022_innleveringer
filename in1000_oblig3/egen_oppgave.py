# Lag et login program. Hvis brukernavnet eller passordet er feil, skal det komme en feilmelding,
#   i tillegg gjenta input av brukernavn/passord

brukere = { # brukere i en dictionary
    "dan123": "abc123",
    "lee3": "abc321",
    "ramo": "cba213"
}


def login_bruker(): # Funksjon som tar inn input brukernavn og sjekker om det finnes i dictionary-en
    input_navn = input("Brukernavn: ")  # Input brukernavn fra bruker
    funnet_brukernavn = False

    for key in brukere: # Går gjennom dictionary-en og sjekker om brukernavn ligger i den
        if key == input_navn:   # Om den finner en brukernavn lik inputen
            funnet_brukernavn = True    # Gjøre verdien til True
            break   # Går ut av for-løkken

    if funnet_brukernavn:   # Om verdien er True
        print("Brukernavn funnet!") # Printer ut melding
        login_passord(input_navn)   # Kjører funksjonen login_passord() med 'input_navn' som argument
    else:   # Hvis brukernavnet ikke var en av de i dictionary-en, kjører koden under
        print('Fant ikke bruker, prøv på nytt!') # Printer ut melding
        login_bruker()  # Kjører denne funksjonen på nytt


def login_passord(brukernavn):  # Funksjon som ber input skrive passordet til brukeren og sjekker om det er lik
    input_passord = input('Skriv inn passord: ') # Input passord fra bruker

    if brukere[brukernavn] == input_passord:    # Hvis passordet til brukeren er lik input
        print('Riktig Passord! Login Vellykket!')   # Printer ut melding
    else:   # Hvis ikke lik, kjører koden under
        print('Feil passord, prøv på nytt!')    # Printer ut melding
        login_passord(brukernavn)   # Kjører funksjonen på nytt


login_bruker()  # Kjører funksjonen for første gang
