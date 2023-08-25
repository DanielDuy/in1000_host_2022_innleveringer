# Be brukeren lage to lister, der du lager en løkke med hver variabel i hver liste. Man skal også kunne fjerne ting
# fra listen etter. F.eks. list1 = a b c d, liste2 = 1 2 3 4, funksjonen gir ny_liste = a 1 b 2 c 3 d 4

liste1 = []
liste2 = []
ny_liste = []

# Spør om input en bokstav 4 ganger
for x in range(4):
    y = input("Skriv en bokstav: ")  # input
    liste1.append(y)  # Legger i listen

# Spør om input et tall 4 ganger
for x in range(4):
    y = input("Skriv en nummer: ")  # input
    liste2.append(y)  # Legger tallet i listen

# Legger elementer fra hver liste i en 'løkke' i den nye listen
for x in range(4):
    ny_liste.append(liste1[x])
    ny_liste.append(liste2[x])

print(ny_liste)


# Spør til slutt om du vil fjerne noen elementer med feil tasting operasjoner.
def fjerne_elementer():  # Funksjon
    input1 = input("Vil du fjerne noe fra listen, \'ja\' eller \'nei\'? Svar: ")  # Input om du vil gjerne element
    if input1 == 'ja':  # Hvis input er 'ja'
        input2 = input('Hvilke element fra lista vil du fjerne? Input: ')  # input element du vil fjerne
        if input2 in ny_liste:  # Hvis elementet finnes i listen
            ny_liste.remove(input2)  # Fjerner elementet fra listen
            print('\'{}\' er fjernet fra listen.'.format(input2))  # Printer melding bekreftelse fjernet
            print(ny_liste)  # Printer ut listen
            fjerne_elementer()  # Kjører programmet på nytt
        else:  # Hvis elementet ikke er i listen
            print('Finner ikke elementet i listen, prøv på nytt.')  # Feil melding
            fjerne_elementer()  # Kjører programmet på nytt
    elif input1 == 'nei':  # Hvis input er nei, avsluttes programmet
        print('Den er grei!')
    else:  # Hvis ugydlig input
        print('Ugyldig svar, prøv på nytt.')  # Printer feilmelding
        fjerne_elementer()  # Kjører programmet på nytt


fjerne_elementer()  # Kjører funksjonen
