import elev
import pickle
import os

class ElevHandler:

    #Konstruktor-----------------------------------
    def __init__(self):
        self.elevlist = []
        self.filename = "elever.pkl"

        try:
            self.read_from_file()

        except ValueError:
            print("Kunde inte läsa in filen " + self.filename)

    def print_meny(self):
        print("------------------------")
        print("\n\tMENY\n")
        print("\t1. Lista elever")
        print("\t2. Lägg till elev")
        print("\t3. Ta bort elev")
        print("\t4. Spara och Avsluta")

        val = input("Gör ett val: ")

        return val
    
    def add_elev(self, elevnamn, utbildning, tel):
        t_elev = elev.Elev(elevnamn, utbildning, tel)
        self.elevlist.append(t_elev)

    def print_elevlist(self):
        self.elevlist = sorted(self.elevlist, key=lambda p: p.namn)

        print("\n-------------------------------\n")
        print("-Lista på Elever-")

        for elev in self.elevlist:
            print(elev.get_elev())

    def del_elev(self):
        print("\nTa bort en elev\n")

        tel = input("Mata in telefonnumret för eleven: ")

        try:
            self.elevlist = [p for p in self.elevlist if p.tel != tel]

        except ValueError:
            print("\nKunde inte ta bort eleven\n")

    def save_to_file(self):
        self.elevlist = sorted(self.elevlist, key=lambda p: p.namn)

        with open(self.filename, "wb") as f:
            pickle.dump(self.elevlist, f)

    def spara_avsluta(self):
        self.save_to_file()

    def read_from_file(self):
        #Om filen saknas
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("")

        else:
            #Öppnar fil för läsning
            with open(self.filename, "rb") as f:
                elever = pickle.load(f)
                self.elevlist = elever