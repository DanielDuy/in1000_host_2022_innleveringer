# Oppretter brukernavn, epost i en dictionary via innputs
# Oppgave 1
def lagBrukernavn(full_navn):  # Definerer funksjon som tar inn et argument
    fornavn_etternavn = full_navn.split(" ")  # Deler navnet i to via split() og " ", og legger begge i en liste
    ny_brukernavn1 = fornavn_etternavn[0] + fornavn_etternavn[1][0]  # Kombinerer fornavn med det første bokstaven i
    #   etternavnet og lagrer det i en variabel
    ny_brukernavn1 = ny_brukernavn1.lower()  # Gjør alle store bokstaver til små bokstaver
    return ny_brukernavn1  # Returnerer navnet


# Oppgave 2
def lagEpost(brukernavn, suffix):  # Definerer funksjoner som tar inn to argumenter
    ny_epost = "{}@{}".format(brukernavn, suffix)  # Lager en epost med å kombinerer argumentene og legge en @ mellom
    return ny_epost  # Returnerer variabelen


# Oppgave 3
def skrivUtEpost(ordboken):  # Definerer en funksjon som tar inn 1 argument (ordbok)
    for x in ordboken:  # Itererer gjennom alle 'key'-ene i dictionary-en
        print(lagEpost(x, ordboken[x]))  # Kaller på lagEpost(brukernavn, suffix) for hver key og value, og lager epost
        #   og deretter printer det ut


test_ordbok = {  # Ordbok for å teste skrivUtEpost(ordboken)
    'olan': 'ifi.uio.no',
    'karin': 'student.matnat.uio.no'
}
skrivUtEpost(test_ordbok)  # Kaller på skrivUtEpost(ordboken) med test_ordbok som argument

# Oppgave 4a, b, c
ordbok = {}  # Tom ordbok
while True:  # En while løkke som itererer for alltid
    print("\nTast \'i\' for å legge til \'navn\' og \'epost-suffix'.")  # Info
    print("Tast \'p\' for å vise epost i database.")  # Info
    print("Tast \'s\' for å avslutte programmet.")  # Info

    y = input("Skriv her: ")  # Tar inn input fra bruker og lagrer det i en variabel

    if y == "i":  # Hvis input er 'i'
        input_brukernavn = input("Skriv inn fornavn og etternavn: ")  # Input fulle navn
        input_epostsuffix = input("Skriv inn e-post suffix: ")  # Input epost suffix
        ny_brukernavn = lagBrukernavn(
            input_brukernavn)  # Kaller på lagBrukernavn(full_navn) med input_brukernavn som argument
        ordbok[ny_brukernavn] = input_epostsuffix  # Legger brukernavnet som key og epost suffix som value i ordbok
    elif y == "p":  # Hvis input er 'p'
        skrivUtEpost(ordbok)  # Kall på skrivUtEpost(ordboken) med ordbok som argument, printer ut alle epostene
    elif y == "s":  # Hvis input er 's'
        break  # Bryter ut av while-løkken
