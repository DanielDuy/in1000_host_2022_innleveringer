# Programmet, ber brukeren oppgi navn, deretter printer ut navnet, beregner differansen av to variabler og legger
#   summen i en ny variabel og deretter skriver ut variabelen. Så spør programmet om en ny input om et navn som vi
#   lagrer i en ny variabel og deretter kombinerer variablene i en ny variabel og printer det ut.

# Oppgave 2, 3
navn_input = input("Oppgi et navn: ")  # Ber brukeren oppgi en tekststreng og lagrer det i en variabel.
print("Hei {}!".format(navn_input))  # Setter variabelen i en streng og printer det ut.

# Oppgave 4
variabel1 = 3
variabel2 = 5
print(variabel1)
print(variabel2)

# Oppgave 5
differansen = variabel1 - variabel2  # Beregner differansen mellom to variabler og lagrer resultatet i en variabel.
print("Differanse: {}".format(differansen))  # Setter variabelen i en streng og printer det ut.

# Oppgave 6, 7
navn_input2 = input("Oppgi et nytt navn: ")  # Ber brukeren oppgi en annen tekststreng og lagrer det i en variabel.
sammen = navn_input + navn_input2  # Kombinerer to streng variabler.
print(sammen)  # Printer ut streng variabelen.

# Oppgave 7
sammen = navn_input + " og " + navn_input2  # endrer variabelen ved å legge til mellomrom og "og" mellom variablene.
print(sammen)  # Printer ut den nye streng variabelen.
