from hund import *


# Oppgave 2
def hovedprogram():
    # Oppgave 6
    hund1 = Hund(7, 25)  # Oppretter objekt
    hund2 = Hund(3, 5)  # Oppretter objekt

    # Printer ut alder, vekt og metthet
    print('|Hund1| Alder: ' + str(hund1.hent_alder()), '  Vekt: ' + str(hund1.hent_vekt()), '  Metthet: ' + str(hund1.metthet))
    print('|Hund2| Alder: ' + str(hund2.hent_alder()), '  Vekt: ' + str(hund2.hent_vekt()), '  Metthet: ' + str(hund2.metthet))

    for x in range(3):  # Hund1 sprinter 6 ganger, mens hund2 springer 3 ganger
        hund1.spring()
        hund1.spring()
        hund2.spring()

    print('|Hund1| Vekt: ' + str(hund1.hent_vekt()), '  Metthet: ' + str(hund1.metthet))
    print('|Hund2| Vekt: ' + str(hund2.hent_vekt()), '  Metthet: ' + str(hund2.metthet))

    hund1.spis(4)  # Metthet + 4
    hund2.spis(3)  # Metthet + 3

    print('|Hund1| Vekt: ' + str(hund1.vekt), '  Metthet: ' + str(hund1.metthet))
    print('|Hund2| Vekt: ' + str(hund2.vekt), '  Metthet: ' + str(hund2.metthet))


hovedprogram()
