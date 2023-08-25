# Oppgave 1
alder = int(input('Skriv inn din alder: ')) # Får in input tall/alder og lagrer i en variabel

# Oppgave 2
billett_pris = 0

# Oppgave 3
if alder <= 17: # Sjekker om alderen er under eller lik 17
    billett_pris = 30   # Endrer billettpris til 30
elif 17 < alder:    # Sjekker om brukeren er over 17
    billett_pris = 50   # Endrer billettpris til 50
elif 63 <= alder:   # Sjekker om alderen er lik eller større enn 63
    billett_pris = 35   # Endrer billettpris til 35

# Oppgave 4
# Printer ut variablene i strenger
print("|--------Enkelt Billett---------|")
print("|- Alder oppgitt: \"{} år\"       |".format(alder))
print("|- Pris for billett: {}.00 kr   |".format(billett_pris))
print("|                               |")
print("|-------------------------------|")

# Oppgave 5
# Det som er galt med denne prosedyren er at den ikke oppgir riktig billett-pris for alder over eller lik 63 år.
#   Det er fordi 63 år er større enn 17, så den setter billett-prisen på alderen voksen og går ut deretter fra
#   if-else-sjekken.
