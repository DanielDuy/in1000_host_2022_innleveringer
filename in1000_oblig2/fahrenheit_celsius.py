# Oppgave 1 (oppgave 5)
tempe_fahrenheit = input("Skriv inn en temperatur i fahrenheit: ")  # Lagrer input i en variabel

is_number = False
while not is_number:    # Ved hjelp av variabelen "is_number", så kjører koden under.
    try:         # Så lenge det kommer en feilmelding når man prøver å konvertere input, kjører programmet på nytt.
        float(tempe_fahrenheit)     # Prøver å konvertere input.
        is_number = True
    except ValueError:  # Om koden ovenfor gir en feilmelding, så kjører koden under.
        is_number = False
        print("Ikke en gydlig tallverdi!")  # Printer
        tempe_fahrenheit = input("Skriv inn en temperatur i fahrenheit: ")

# Oppgave 2
print(tempe_fahrenheit)

# Oppgave 3
tempe_celsius = (float(tempe_fahrenheit) - 32) * 5 / 9  # Konverterer fahrenheit til celsius

# Oppgave 4
print(format(tempe_celsius, ".2f")) # Minsker komma til 2 tall

# Oppgave 5
# Se oppgave 1, 2, 3, 4
