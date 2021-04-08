# Introduzione
print("Ciao, sono un programma intelligente! Mio padre è Alessandro Jelveh. Mi piace giocare con i numeri :)")
# Linee codice per riconoscere se il numero è pari o dispari
def program():
    numero_preferito = int(input("Qual è il tuo numero preferito? "))
    if numero_preferito % 2 == 0:
        print("Il tuo numero preferito è pari :)")
    else:
        print("Il tuo numero preferito è dispari :)")
# Linee codice per ripetere
flag = True
while flag:
    program()
    flag = input("Rifacciamo? ")
    if (flag == "si") or (flag == "ok") or (flag == "va bene") or (flag == "daje") or (flag == "sì") or (flag == "s"):
        print("Ok!")
    else:
        flag = False
# Conclusione
print("Va bene, a presto!")