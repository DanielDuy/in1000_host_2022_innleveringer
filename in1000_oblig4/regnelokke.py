# Oppgave 1,2
input_num = 1
lst_input = []
while input_num != 0:  # Når input ikke er 0, kjører koden under
    input_num = int(
        input("Skriv inn et nummer: "))  # Tar inn en input og gjør det om til en int og lagrer det i en variabel
    if input_num != 0:  # Hvis input ikke er 0,
        lst_input.append(input_num)  # legger tallet i listen

# Oppgave 3
for x in lst_input:  # En for løkke som går gjennom lista
    print(x)  # Printer ut hvert element

# Oppgave 4
minSum = 0
for x in lst_input:  # Går gjennom alle elementene i listen
    minSum += x  # plusser elementene i en variabel
print("Summen: {}".format(minSum))  # Printer ut summen

# Oppgave 5
minimum = lst_input[0]  # Setter den første tallet i listen som min i en variabel
for x in lst_input:  # For løkke som går gjennom alle elementene i listen
    if x < minimum:  # Sjekker om x er mindre enn minimum
        minimum = x  # Om x er mindre enn minimum, setter vi x som nye minimum
print("Minimum: {}".format(minimum))  # Printer it minimum i en streng

maksimum = lst_input[0]  # Setter den første tallet i listen som maks i en variabel
for x in lst_input:  # For løkke som går gjennom alle elementene i listen
    if maksimum < x:  # Sjekker om elementet i listen er større en maksimum
        maksimum = x  # Om x er større enn maksimum, setter vi x som nye maksimum
print("Maksimum: {}".format(maksimum))  # Printer ut maksimum i en streng
