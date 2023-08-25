# Porgram som printer ut spørsmål og tar imot input. den printer string basert på inputs.

# Oppgave 1
print("Svar enten \"ja\" eller \"nei\"")
svar1 = input("Liker du brus? Svar: ")  # Ber brukeren skrive inn en streng som blir lagret i en variabel.

# Oppgave 2a
if svar1 == "ja":                       # Hvis brukeren skrev "ja", vil det under printes ut.
    print("Her har du en brus!")
# Oppgave b
elif svar1 == "nei":                    # Hvis brukeren skrev "nei", vil det under printes ut.
    print("Den er grei.")
# Oppgave c
else:                                   # Hvis brukeren skrev ingen av delene, vil det under printes ut.
    print("Det forstod jeg ikke helt.")
