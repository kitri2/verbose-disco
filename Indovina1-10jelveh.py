# Secondo me è meglio così: il programma sceglie un numero, e quel numero rimane.
# Quando lo indovini il programma termina con la funzione sys.exit
# Dobbiamo ancora risolvere la questione dell'input str
# Devo rendere più naturali le str del programma

import random
import sys

print("Ciao, sono figlio di Edoardo Dal Prà e Alessandro Jelveh. Mi piace giocare con i numeri!")

random_number = random.randint(1, 10)

# Funzione principale


def program():
    numero_input = int(input("Sto pensando a un numero da 1 a 10, quale? "))

    if numero_input <= 10:
        if random_number == numero_input:
            print("Esatto!")
        if random_number == numero_input:
            sys.exit("Ciao, a presto!")
        else:
            print("Sbagliato!")

    if numero_input > 10:
        print("Non vale!")


# Funzione di opzione restart del codice
flag = True
while flag:
    program()
    flag = input("Rifacciamo? ")
    if (flag == "si") or (flag == "ok") or (flag == "va bene") or (flag == "daje") or (flag == "sì") or (flag == "s"):
        print("Ok, vediamo...")
    else:
        flag = False

print("Va bene, a presto!")
