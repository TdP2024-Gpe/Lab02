import translator as tr
import dictionary as dc

import menu as mn

t = tr.Translator()

d = dc.Dictionary()

m = mn.Menu()

path_file = "dictionary.txt"

d.loadDictionary(path_file)

# print(d._dict)
# print(d._dict.keys())
# print(d._dict["kissa"])
# print(d._dict["kissa"][1])

while True:

    m.print_menu()

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("")
        print("Ok, quale parola devo aggiungere?")
        print("")
        txtIn = input()
        print("\n", t.handle_add(txtIn, path_file))
        continue

    if int(txtIn) == 2:
        print("")
        print("Ok, quale parola devo cercare?")
        print("")
        txtIn = input()
        print("\n", t.handle_translate(txtIn))
        continue

    if int(txtIn) == 3:
        print("Ok, inserisci la wildcard da cercare?")
        txtIn = input()
        continue

    if int(txtIn) == 4:
        print("")
        print("Ok, ecco tutto il dizionario: ")
        print("")
        d.print_all()
        continue

    if int(txtIn) == 5:
        print("")
        print("Ciao! ti aspetto per le prossime traduzioni")
        print("")
        break
