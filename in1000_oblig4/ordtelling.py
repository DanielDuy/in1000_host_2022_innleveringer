# Oppgave 1
def antall_bokstaver(ordet):  # En funsjon tar inn en argument
    return len(ordet)  # Funksjonen returnerer lengden av ordet


# Oppgave 2
def ordbok(setning):
    ordboken = setning.split()  # Splitter setningen basert på mellomrom i en liste, slik at vi får hvert ord
    print("Det er {} ord i setningen.".format(len(ordboken)))  # Printer ut antall ord i setningen

    # Lager en nye liste som kun inneholder unike ord
    unike_ord_liste = [ordboken[0]]  # Liste men kun unike ord
    for x in range(1, len(ordboken)):  # Går gjennom nylig lagd liste
        if ordboken[x] not in unike_ord_liste:  # Hvis ordet ikke er i den nye listen,
            unike_ord_liste.append(ordboken[x])  # Så blir ordet lagt i den nye listen

    # Teller antallet ganger ordet gjentar i setningen
    liste_antall = []  # Skal inneholde antallet
    for x in unike_ord_liste:  # Går gjennom hvert unike ord
        teller = 0  # Skal telle hvor mange ganger ordet gjentas
        for y in ordboken:  # Går gjennom listen med alle ordene
            if x == y:  # Hvis den unike ordet er lik ordet i listen
                teller += 1  # Plusser antallet
        liste_antall.append(teller)  # Legger til antallet i listen

    # Legger det unike ordet og antall ganger gjentatt i en dictionary
    dictionary_ordbok = {}
    for x in range(len(unike_ord_liste)):  # Går gjennom lengden av listen, unike_ord_liste
        dictionary_ordbok[unike_ord_liste[x]] = liste_antall[x]  # Legger ordet og antall ganger gjentatt som en element

    return dictionary_ordbok  # Returnerer dictionary ordboken


def ordtellinga():
    ordbok_dict = ordbok(input("Skriv en setning her: "))  # Input en setning og kjører funksjonen og lagrer dict i en
    # variabel

    # Printer ut dictionary-en i en streng
    for key in ordbok_dict:  # Går gjennom hver nøkkelverdi i dictionary-en
        if (ordbok_dict[key] == 1) and (
                antall_bokstaver(key) == 1):  # Hvis antall ganger gjentatt er 1 og inneholder 1 bokstav
            print("\nOrdet \'{}\' forekommer {} gang, og har {} bokstav".format(key, ordbok_dict[key],
                                                                                antall_bokstaver(key)))
        elif (ordbok_dict[key] == 1) and (
                antall_bokstaver(key) > 1):  # Hvis antall ganger gjentatt er 1 og inneholder mer enn 1 bokstav
            print("\nOrdet \'{}\' forekommer {} gang, og har {} bokstaver".format(key, ordbok_dict[key],
                                                                                  antall_bokstaver(key)))
        elif (ordbok_dict[key] > 1) and (
                antall_bokstaver(key) == 1):  # Hvis antall ganger gjentatt er mer enn 1 og inneholder 1 bokstav
            print("\nOrdet \'{}\' forekommer {} ganger, og har {} bokstav".format(key, ordbok_dict[key],
                                                                                  antall_bokstaver(key)))
        elif (ordbok_dict[key] > 1) and (
                antall_bokstaver(key) > 1):  # Hvis antall ganger gjentatt er mer enn 1 og inneholder mer enn 1 bokstav
            print("\nOrdet \'{}\' forekommer {} ganger, og har {} bokstaver".format(key, ordbok_dict[key],
                                                                                    antall_bokstaver(key)))


ordtellinga()  # Kjører funksjonen
