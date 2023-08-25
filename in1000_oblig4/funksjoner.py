# Oppgave 1
def adder(tall1, tall2):  # Definerer funksjonen som tar inn to argumenter
    summ = tall1 + tall2  # Summerer argumentene og lagrer det i en variabel
    return summ  # Returnerer summen


print("{} + {} = {}".format(3, 5, adder(3, 5)))  # Bruker funksjonen og setter det i en streng
print("{} + {} = {}".format(4, 9, adder(4, 9)))  # Bruker funksjonen og setter det i en streng

# Oppgave 2, 3
inp_tkst_strg = input("Skriv inn en tekststreng: ")  # Får input om en tekst streng
inp_bokstav = input("Skriv inn en bokstav: ")  # Får input om en bokstav streng


def tellForekomst(minTekst, minBokstav):  # Definerer funksjon med to argumenter
    antall = 0  # Antall ganger et tall skal gjentas
    for x in minTekst:  # For-løkke som kjører gjennom strengen
        if x == minBokstav:  # Sjekker om bokstaven i strengen er lik bokstav input
            antall += 1  # Legger til i sum
    print(antall)  # Printer ut antall ganger gjentatt


tellForekomst(inp_tkst_strg, inp_bokstav)  # Kjører funksjonen
