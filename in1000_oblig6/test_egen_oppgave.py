from egen_oppgave import *

# Oppgave 2
input_navn = input('skriv inn navn: ')  # Input navn

input_alder = input('skriv inn alder: ')  # Input alder

p1 = Person(input_navn, input_alder)  # Oppretter objekt med inputs

input_hobby = input('Legg til hobby (Press enter uten input for å avslutte): ')  # Legg til hobby ved input
while input_hobby != '':  # Hvis input ikke er en tom streng/''
    p1.leggTilHobby(input_hobby)  # Legg strengen/hobbye i listen
    input_hobby = input('Legg til hobby (Press enter uten input for å avslutte): ')  # Samme input

p1.skrivUt()  # Skriver ut navnet, alder og hobbyen til funksjonen
