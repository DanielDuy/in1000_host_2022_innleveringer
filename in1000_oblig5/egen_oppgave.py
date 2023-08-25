# Oppgave 1
# Eller du kan følge dette forslaget: Skriv et beregningsprogram for skreddere med en funksjon som leser inn en fil
#   (som du lager selv og leverer sammen med de andre filene) der hver linje beskriver et navn på et mål og selve målet
#   i tommer. Formatet vil se slik ut:
#       Skuldervredde 4
#       Halsvidde 3.2
#       Livvidde 10
# Hint: du kan bruke funksjonen .split() for å gjøre dette.
# La programmet legge disse målene i en ordbok med nav på målet som nøkkelverdi og returnerer  ordboken. Lag deretter en
#   prosedyre som tar imot en liste av mål og benytter seg av tommerTilCm som du skrev tidligere for å skrive ut målene
#   i centimeter.

# Oppgave 2
def les_oprett_ordbok(
        filnavn):  # Funksjon som skal lese inn en fil, lagre tingene i filen i en dictionary, også returne
    #                               dictionaryen.
    file = open(filnavn)  # Åpner filen

    ny_ordbok = {}  # Her skal innholdet fra filen ligge

    for linje in file:  # For hver linje i filen
        oppdelt_linje = linje.split()  # Splitter linjen basert på ' ', i to, og legger delene i en array
        ny_ordbok[oppdelt_linje[0]] = oppdelt_linje[1]  # Legger begge delene i dictionaryen

    file.close()  # Lukker filen

    return ny_ordbok  # Returnerer ordboken


ordbok1 = les_oprett_ordbok('fil_til_egen_oppgave')  # Kaller på funksjonen ovenfor med den vedlagte filen som argument


def skriv_ut_mal(ordbok):  # Funksjon som tar inn dictionary som argument og printer ut tingene i dictionary-en
    for key in ordbok:  # For hver nøkkel i dictionaryen
        cm = float(ordbok[key]) * 2.54  # Gjør om verdien fra hver nøkkel til float og omgjør tallet i cm(* 2.54)
        print(key, cm)  # Printer ut nøkkelen og tallet


skriv_ut_mal(ordbok1)  # Kaller på funksjonen med ordboken lagd ovenfor fra den andre funksjonen som argument
