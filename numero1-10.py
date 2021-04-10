# documentazione amica: forse forse non dovremo pensare a usare except, try ed exceptions handlers vari: alla fine
# daranno ValueError in rosso come al solito, non quello che vogliamo (un finto messaggio di errore,
# non uno spaventavecchi)

# HO CAPITO FLAG, ma ho anche trovato su Stack un sistema simile che proverei ad implementare
# su un branch locale della repo

# Salvati tutto quello che trovi nella repo, con me al comando nulla è al sicuro.


import random

print("Ciao, sono figlio di Edoardo Dal Prà e Alessandro Jelveh. Mi piace giocare con i numeri!")



# funzione program


def program():
    random_number = random.randint(1, 10)

    numero_input = int(input("Sto pensando a un numero da 1 a 10, quale? "))

    if numero_input <= 10:
        if random_number == numero_input:
            print("Esatto!")
        else:
            print("Sbagliato!")

    if numero_input > 10:
        print("Non vale!")


# funzione restart del codice
flag = True
while flag:
    program()
    flag = input("Rifacciamo? ")
    if (flag == "si") or (flag == "ok") or (flag == "va bene") or (flag == "daje") or (flag == "sì") or (flag == "s"):
        print("Ok, vediamo...")
    else:
        flag = False
