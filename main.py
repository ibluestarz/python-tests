#!/bin/python3

def name(lan):
    if lan == "EN":
        prompt = "What is your name ?\n"
    elif lan == "FR":
        prompt = "Quel est votre nom ?\n"
    elif lan == "ES":
        prompt = "Como te llama ?\n"
    nom = input(prompt).lower()
    nom = nom[0].upper() + nom[1:]
    if nom == "":
        nom = "Anonymous"
    return nom

def lang():
    ## Check:
    langue = "" 
    while langue not in ["EN","FR","ES"]:
        langue = input("Choose a language : \nEN for English,\nFR en français,\nES enespañol :\n").upper()
    ## Fin check
    nom = name(langue)
    if langue == "EN":
        prompt = "Hello"
    elif langue == "FR":
        prompt = "Bonjour"
    elif langue == "ES":
        prompt = "Hola"
    print(prompt, nom)
    return prompt, nom, langue

def byelang(lan):
    if lan == "EN":
        prompt = "Bye"
    elif lan == "FR":
        prompt = "Aurevoir"
    elif lan == "ES":
        prompt = "Ciao"
    return prompt

## Main
prompt, nom, langue = lang()
cmd = "" 
settings = ""
byelang = byelang(langue)
while cmd != "quit":
    cmd = input(prompt + " " + nom + ": $ ")

    if cmd == "hello":
        print(prompt + " " + nom)
    elif cmd == "settings":
        if langue == "FR":
            print("Quel paramètre souhaitez-vous modifier ?\n")
            settings = input("PROMPT, NAME, LANG \n").upper()
            if settings == "PROMPT":
                prompt = input("Ecrivez ce que vous voulez afficher \n")
            elif settings == "NAME":
                nom = name(langue)
            elif settings == "LANG":
                langue = input("Choisissez un langage : \nEN for English,\nFR en français,\nES enespañol :\n").upper()
        elif langue == "EN":
            print("Choose the setting you want to change ? \n")
            settings = input("PROMPT, NAME, LANG").upper()
            if settings == "PROMPT":
                prompt = input("What do you want to display ?\n")
            elif settings == "NAME":
                nom = name(langue)
            elif settings == "LANG":
                langue = input("Choose a language : \nEN for English,\nFR en français,\nES enespañol :\n").upper()
        elif langue == "ES":
            print("¿Qué configuración quieres cambiar? \n")
            settings = input("PROMPT, NAME, LANG \n").upper()
            if settings == "PROMPT":
                prompt = input("Escribe lo que quieres mostrar \n")
            elif settings == "NAME":
                nom = name(langue)
            elif settings == "LANG":
                langue = input("Elige un idioma : \nEN for English,\nFR en français,\nES enespañol :\n").upper()

    elif cmd == "help":
        if langue == "FR":
            print(">>> Liste des commandes :") 
            print("~ hello : L'ordinateur vous salue.")
            print("~ quit : Permet de quitter le programme, l'ordinateur vous dit aurevoir")
            print("~ settings : Pour modifier un paramètre")
            print("~ help : permet d'ouvrir d'afficher les commandes \n")

        elif langue == "EN":
            print(">>> All commands :")
            print("~ hello : The computer says hello.")
            print("~ quit : Leave the program, the computer says goodbye")
            print("~ settings : To change settings")
            print("~ help : displays all commands \n")

        elif langue == "ES":
            print(">>> Lista de comandos :")
            print("~ hello : la computadora te saluda")
            print("~ quit : sale del programa, la computadora se despide")
            print("~ settings : para cambiar la configuración")
            print("~ help : muestra la lista de commandos \n")
    else:
        if langue == "FR":
            print("*** Pour voir la liste des commandes, écrivez : help ***")
        elif langue == "EN":
            print("*** To see all commands, type : help ***")
        elif langue == "ES":
            print("*** Para ver la lista de comandos, escriba : help ***")

print(byelang + " " + nom + " !")


## Fin main




