import random

print("Ciao, sono figlio di Edoardo Dal Prà e Alessandro Jelveh. Mi piace giocare con i numeri!")

random_number = random.randint(1, 10)

# funzione program
def program():
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
