def pari():
    x = int(input("INPUT X"))
    if x % 2 == 0:
        print("x è pari")
    else:
        print("x è dispari")


pari()

restart = input("Riprovare?(s/n)")
if restart == "s":
    pari()
else:
    print("pacco")

# controllo branch repo
