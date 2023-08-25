# Oppgave 1
lst = [3, 7, 11]  # liste med 3 tall
lst.append(15)  # Legger til et nytt tall i lista ovenfor
print(lst[0], lst[2])  # Printer ut første og tredje element fra lista ovenfor

# Oppgave 2
navn_liste = []  # Ny tom liste
navn_liste.append(input('Oppgi et navn: '))  # Input et navn og legger det til listen ovenfor
navn_liste.append(input('Oppgi et til navn: '))  # --||--
navn_liste.append(input('Oppgi et til navn: '))  # --||--
navn_liste.append(input('Oppgi et til navn: '))  # --||--

# Oppgave 3
if "Daniel" in navn_liste:  # Sjekker om navnet mitt ligger i listen
    print('Du husket meg!')
else:
    print('Glemte du meg?')

# Oppgave 4
sum_lst = sum(lst)  # Summerer alle elementene i den første listen

produkt_lst = lst[0]    # Angir variabelen som første element fra tall listen
for x in range(1, len(lst)):  # For løkke som kjører basert på lengden av listen, men starter på 1
    produkt_lst = produkt_lst * lst[x]  #  Angir variabelen som variabelen gange et nytt tall

ny_lst = [sum_lst, produkt_lst] # Legger variablene i en ny liste

kombinert_lst = lst + ny_lst    # Kombinerer to lister i en ny liste
print(kombinert_lst)    # Printer ut den nye listen

del kombinert_lst[-2:]  # Sletter de to siste elementene fra listen
print(kombinert_lst)    # Printer ut listen igjen
