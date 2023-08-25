def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return (b)


def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print(b)
    print(a)


hovedprogram()

# Først defineres funksjon minFunksjon() (ingen parametre).
# Deretter defineres hovedprogram() (ingen parametre).
# Deretter kalles hovedprogram().
#   Variabel a opprettes med verdi 42.
#   Variabel b opprettes med verdi 0.
#   Variabelens a blir printet i konsoll.
#   Variabel b blir tilordnet til verdi b.
#   Variabel a blir tilordnet til verdi fra minFunksjon()
#       En for-løkke skal kjøre 2 ganger.
#           Variabel c blir opprettet med verdi 2.
#           Variabel c blir printet i konsoll.
#           Variabel c blir tilordnet seg selv + 1.
#           Variabel b blir opprettet med verdi 10.
#           Variabel b blir tilordnet seg selv + a. (a er ikke en tilgjengelig variabel for funksjonen, derfor stoppes
#               programmet med feilmelding.)