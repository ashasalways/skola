import elevhandler


looping = True

skola = elevhandler.ElevHandler()



while looping:
    val = skola.print_meny()

    if (val == "1"):
        print("\nlista elever\n")

    elif (val == "2"):
        namn = input("Mata in namnet: ")
        utb = input("Mata in utbildningen: ")
        tel = input("Mata in telefonnumret")

    elif (val == "3"):
        print("\nremove elev\n")

    elif (val == "4"):
        break