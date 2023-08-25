# Program som leser inn dag og måned to ganger, den printer basert på rekkefølgen mellom dato inputene.

# Oppgave 1
dato1_dag = int(input("Skriv inn dato (dag) her: "))
dato1_maned = int(input("Skriv inn dato (måned) her: "))

dato2_dag = int(input("Skriv inn dato (dag) her: "))
dato2_maned = int(input("Skriv inn dato (måned) her: "))

# Oppgave 2
# sjekker om første dato er før andre dato
if dato1_maned < dato2_maned or (dato1_dag < dato2_dag and dato1_maned == dato2_maned):
    print("Riktig rekkefølge!")
# Sjekker om første dato er før andre dato
elif dato1_maned > dato2_maned or (dato1_dag > dato2_dag and dato1_maned == dato2_maned):
    print("Feil rekkefølge!")
else:   # Hvis de to første if ikke er sanne, så er datoene like
    print("Samme dato!")
