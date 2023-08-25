varer = {   # Lager dictionary
    'melk': 14.90,
    'brød': 24.90,
    'yoghurt': 12.90,
    'pizza': 39.90
}

vare_navn1 = input('Varenavn: ')    # Lagrer varenavn input i en variabel
vare_pris1 = float(input('Prisen til varen: ').format('.2f'))   # Lagrer varepris input i en variabel

varer[vare_navn1] = vare_pris1  # Legger den nye varen med hjelp av vare-navn og -pris variablene

vare_navn2 = input('Varenavn: ')    # Gjentar prosessen ovenfor med nye variabler
vare_pris2 = float(input('Prisen til varen: ').format('.2f'))

varer[vare_navn2] = vare_pris2

print(varer)    # Printer ur dictionary-en
