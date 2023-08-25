# Leser filer, lagrer filer i deler og sammenlikner dem. Til slutt overskriver en av filene.
# Oppgave 1
def opprette_ordbok(filnavn):  # Funksjon som skal lage en ordbok utfra måneder som keys og temperaturene som values
    file = open(filnavn)  # Åpner filen via argumentet
    ny_ordbok = {'Jan': [], 'Feb': [], 'Mar': [], 'Apr': [], 'May': [], 'Jun': [], 'Jul': [], 'Aug': [], 'Sep': [],
                 'Oct': [], 'Nov': [], 'Dec': []}  # Ny ordbok der keys er månedene

    liste = []  # Tom liste som skal inneholde alle verdiene fra filen
    for linje in file:  # Går gjennom hver linje i filen
        liste.append(linje.split(','))  # Splitter hver linje via ',' og legger alt i en ny list, også list i liste

    for key in ny_ordbok:  # For hver key/måned i ny_ordbok
        for linje in liste:  # For hver linje i listen
            if linje[0] == key:  # Hvis "første objekt i listen" er lik "key i ordbok"
                ny_ordbok[linje[0]].append(float(linje[2]))  # Fra samme linje, legg temperatur i ordboken,
                #                                                tilsvarende måned

    file.close()  # Lukker filen
    return ny_ordbok  # Returnerer ordboken


ordbok1 = opprette_ordbok('max_daily_temperature_2018.csv')  # Kaller på funksjonen med 'max_daily_temperature_2018.csv'
#                                                                   som argument. Lagrer ordboken i variabelen ordbok1.


# Oppgave 2
def sjekk_maks_temp(ordbok, filnavn):  # Funksjon som skal sammenlikne maks temperatur fra i fjor med temperatu fra i år
    file = open(filnavn)  # Åpner filen

    liste = []  # Skal inneholde alle linjene fra filen
    for linje in file:  # Går gjennom hver linje i filen
        liste.append(linje.split(','))  # Deler opp filen basert på komma og legger variablene i en ny liste, så i liste

    nye_rekorder = {}  # Dictionary som skal inneholde måneder og rekord temperaturer

    maned = 0  # "Måneds dato"-1 (Er måneden for maks tempe. som skal sammenliknes)
    for key in ordbok:  # For hver key/måned i ordboken
        if max(ordbok[key]) > float(liste[maned][1]):  # Hvis "maks temperatur" er større enn "maks temperatur"
            # Printer ut melding med variabler satt i strengen. Finner dags dato med index()
            print('Ny varmerekord på {} {}: {} grader Celcius (gammel varmerekord var {} grader Celciues)'.format(
                ordbok[key].index(max(ordbok[key])) + 1, key, max(ordbok[key]), liste[maned][1]))
            nye_rekorder[key] = str(max(ordbok[key])) + '\n'  # Legger måneden og rekord temperaturen i dictionary-en
        maned += 1  # Sjekker neste måned

    for key in nye_rekorder:  # For hver måned som fikk ny rekord
        for linje in liste:  # For hver linje i listen/file
            if key == linje[0]:  # Hvis måneden for rekorden er like måneden fra listen
                linje[1] = nye_rekorder[key]  # Bytter gamle temperatur med den nye rekord temperaturen
                break  # avslutter andre for-løkke

    ny_csv_max = ""  # Skal være det nye innholdet til den nye .csv filen, for max_temperatures_per_month.csv

    for linje in liste:  # For hver linje av liste/kopi av .csv filen
        ny_csv_max += linje[0] + ',' + linje[1]  # Legg måneden + ',' + temperaturen i strengen

    file.close()  # Lukker filen

    file = open(filnavn, 'w')  # Åpner filen for skriving

    file.write(ny_csv_max)  # Erstatter alt i filen med ny_csv_max strengen

    file.close()  # Lukker filen


sjekk_maks_temp(ordbok1, 'max_temperatures_per_month.csv')  # Kaller på prosedyren med ordbok1 og den andre filen som
# argumenter
