# Oppgave 1
steder = []
for n in range(5):  # For løkke som gjentar 5 ganger
    x = input("Sted: ")  # Input fra bruker og lagrer i en variabel
    steder.append(x)  # Legger variabelen i en liste

# Oppgave 2
klesplagg = []
for n in range(5):  # For løkke som gjentar 5 ganger
    x = input("Klesplagg: ")  # Input fra bruker og lagrer i en variabel
    klesplagg.append(x)  # Legger variabelen i en liste

avreisedatoer = []
for n in range(5):  # For løkke som gjentar 5 ganger
    x = input("Avreisedatoer: ")  # Input fra bruker og lagrer i en variabel
    avreisedatoer.append(x)  # Legger variabelen i en liste

# Oppgave 3
reiseplan = [steder, klesplagg, avreisedatoer]  # Legger de 3 listene i en ny liste

# Oppgave 4
for x in reiseplan:  # går gjennom de 3 listene i listen reiseplan
    print(x)  # Printer ut hver liste

# Oppgave 5a
liste_indeks1 = int(input("Skriv et tall mellom 0-2: "))  # Input fra brukeren, gjør det om til int og lagrer det i en
# variabel

# Oppgave b
liste_indeks2 = int(input("Skriv et tall mellom 0-4: "))  # Input fra brukeren, gjør det om til int og lagrer det i en
# variabel

# Oppgave c
if (liste_indeks1 < 0) or (2 < liste_indeks1):  # Hvis første indeks er mindre enn 0 eller større enn 2,
    print("Ugyldig input for indeks 1!")  # Printer ut feilmelding
elif (liste_indeks2 < 0) or (4 < liste_indeks2):  # Hvis andre indeks er mindre enn 0 eller større enn 4,
    print("Ugyldig input for indeks 2!")  # Printer ut feilmelding
else:
    print(reiseplan[liste_indeks1][liste_indeks2])  # Ellers printer ut elementet via indeksene i listen reiseplan
