#!/bin/python3

##############################################################################################################
##############################################################################################################

## IMPORT 
from src.settings import lang, settings, help, info
import src.settings as cmd_set ## exemple : cmd_set.lang ou cmd_set.settings

##############################################################################################################

## INITIALISATION FONCITONS
## fonction bye pour dire aurevoir lorsqu'on quitte le programme dans la langue adaptée
def byelang(langue):
    """
    It takes a language code as input and returns a goodbye message in that language
    
    Args:
      langue: The language to use.
    
    Returns:
      The prompt is being returned.
    """
    if langue == "EN":
        prompt = "Bye"
    elif langue == "FR":
        prompt = "Aurevoir"
    elif langue == "ES":
        prompt = "Ciao"
    return prompt

def apl_help(langue):
    """
    It prints a message to the user, depending on the language they chose
    
    Args:
      langue: The language in which the help message will be displayed.
    
    Returns:
      the string "help"
    """
    if langue == "FR":
            print("*** Pour voir la liste des commandes, écrivez : help ***")
    elif langue == "EN":
            print("*** To see all commands, type : help ***")
    elif langue == "ES":
            print("*** Para ver la lista de comandos, escriba : help ***")
    return


## MAIN
prompt, nom, langue = lang() ## on rappelle les variables de la fonction 
cmd = "" 
# A while loop that will keep running until the user types quit.
while cmd != "quit":
    cmd = input(prompt + " " + nom + ": $ ")

## COMMANDES
    if cmd == "hello": #pour dire bonjour a l'ordinateur
        print(prompt + " " + nom)
    elif cmd == "settings": #pour modifier les parametres
        nom, langue, prompt = settings(nom,langue,prompt)   
    elif cmd == "help": #si l'utilisateur appelle la commande help 
        help(langue)
    elif cmd == "info":
        info(langue,nom,prompt)
    else: #si l'utilisateur execute une commande qui n'existe pas
        if cmd != "quit":
            apl_help(langue)

   
print(byelang(langue) + " " + nom + " !") #si l'utilisateur écrit quit ce message s affiche


## FIN MAIN




