from dato import *

# Oppgave 2
# a.
d1 = Dato(15, 9, 2021)  # Oppretter objekt

# Oppgave 4
# a.
print(d1.hent_aar())  # Printer ut året til objektet

# b.
if d1.dag == 15:  # Hvis dagen til objektet er 15
    print('Loenningsdag!')
elif d1.dag == 1:  # Hvis dagen til objektet er 1
    print('Ny maaned, nye muligheter')

# c.
dato = d1.skrivUtIStreng()

# d.
print(dato)
