# Program som leser inn dag og måned to ganger, den printer basert på rekkefølgen mellom dato inputene.

# Oppgave 3
print("Skriv in datoene slik: 24.Desember = 24.12")

dato1 = input("Skriv inn dato (dag.måned) her: ")
dato1_dag = int(dato1[0:2])                         # Lagrer de to første tallene fra input.
dato1_maned = int(dato1[3:])                        # Lagrer de to siste tallene fra input.

dato2 = input("Skriv inn dato (dag.måned) her: ")
dato2_dag = int(dato2[0:2])                         # Lagrer de to første tallene fra input.
dato2_maned = int(dato2[3:])                        # Lagrer de to siste tallene fra input.

# sjekker om første dato er før andre dato
if dato1_maned < dato2_maned or (dato1_dag < dato2_dag and dato1_maned == dato2_maned):
    print("Riktig rekkefølge!")
# Sjekker om første dato er før andre dato
elif dato1_maned > dato2_maned or (dato1_dag > dato2_dag and dato1_maned == dato2_maned):
    print("Feil rekkefølge!")
else:  # Hvis de to første if ikke er sanne, så er datoene like
    print("Samme dato!")
