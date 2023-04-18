import elevhandler


looping = True

skola = elevhandler.ElevHandler()



while looping:
    val = skola.print_meny()

    if (val == "1"):
        skola.print_elevlist()
        input("\nTryck enter för att fortsätta!\n")

    elif (val == "2"):
        namn = input("Mata in namnet: ")
        utb = input("Mata in utbildningen: ")
        tel = input("Mata in telefonnumret: ")

        skola.add_elev(namn, utb, tel)

    elif (val == "3"):
        skola.del_elev()

    elif (val == "4"):
        skola.save_to_file()
        break
    else:
        print("\nOgiltigt val!\n")