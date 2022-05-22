## fonction langue
def lang():
    """
    The function lang() asks the user to choose a language, then asks for their name, and then prints a
    greeting in the chosen language
    
    Returns:
      the prompt, the name and the language.
    """
    ## Check:
    langue = "" 
    while langue not in ["EN","FR","ES"]: #permet d'afficher le message lorsque l utilisateur n a pas fait de choix
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

## fonction name
def name(lan):
    """
    It asks the user for their name, and returns it
    
    Args:
      lan: The language the user wants to use.
    
    Returns:
      The name of the user
    """
    if lan == "EN":
        prompt = "What is your name ?\n"
    elif lan == "FR":
        prompt = "Quel est votre nom ?\n"
    elif lan == "ES":
        prompt = "Como te llama ?\n"
    nom = input(prompt).lower()
    nom = nom[0].upper() + nom[1:]
    if nom == "": ## Si aucun nom n'est entré, l'utilisateur s'appelle anonymous
        nom = "Anonymous"
    return nom ## on retourne le nom pour l'utiliser apres

## fonction settings
def settings(nom,langue,prompt):
    """
    The function settings() takes three arguments: nom, langue, and prompt. It then asks the user to
    choose a setting to change. If the user chooses to change the prompt, the function asks the user to
    enter a new prompt. If the user chooses to change the name, the function calls the name() function.
    If the user chooses to change the language, the function asks the user to enter a new language. The
    function then returns the new values of nom, langue, and prompt
    
    Args:
      nom: the name of the user
      langue: the language of the program
      prompt: the prompt that will be displayed when the user is asked to enter a command
    
    Returns:
      the name, the language and the prompt.
    """
    if langue == "FR":
        print("Quel paramètre souhaitez-vous modifier ?\n")
        settings = input("PROMPT, NAME, LANG \n").upper()
        if settings == "PROMPT":
            prompt = input("Ecrivez ce que vous voulez afficher \n")
        elif settings == "NAME":
            nom = name(langue)
        elif settings == "LANG":
            langue = input("Choisissez un langage : \nEN for English,\nFR en français,\nES enespañol :\n").upper()
            if prompt == "Bonjour":
               if langue == "ES":
                prompt = "Hola"
               elif langue == "EN":
                prompt = "Hello"
               else:
                prompt = "Bonjour" 
    elif langue == "EN":
        print("Choose the setting you want to change ? \n")
        settings = input("PROMPT, NAME, LANG \n").upper()
        if settings == "PROMPT":
            prompt = input("What do you want to display ?\n")
        elif settings == "NAME":
            nom = name(langue)
        elif settings == "LANG":
            langue = input("Choose a language : \nEN for English,\nFR en français,\nES enespañol :\n").upper()
            if prompt == "Hello":
               if langue == "FR":
                prompt = "Bonjour"
               elif langue == "ES":
                prompt = "Hola"
               else:
                prompt = "Hello" 
    elif langue == "ES":
        print("¿Qué configuración quieres cambiar? \n")
        settings = input("PROMPT, NAME, LANG \n").upper()
        if settings == "PROMPT":
            prompt = input("Escribe lo que quieres mostrar \n")
        elif settings == "NAME":
            nom = name(langue)
        elif settings == "LANG":
            langue = input("Elige un idioma : \nEN for English,\nFR en français,\nES enespañol :\n").upper()
            if prompt == "Hola":
               if langue == "FR":
                prompt = "Bonjour"
               elif langue == "EN":
                prompt = "Hello"
               else:
                prompt = "Hola"  
    return nom, langue, prompt

## fonction help
def help(lan):
    """
    It displays all the commands available in the program.
    
    Args:
      lan: language
    
    Returns:
      nothing.
    """
    if lan == "EN":
        print(">>> All commands :")
        print("~ hello : The computer says hello.")
        print("~ quit : Leave the program, the computer says goodbye")
        print("~ settings : To change settings")
        print("~ info : informations about language, name and prompt")
        print("~ help : displays all commands \n")
    elif lan == "FR":
        print(">>> Liste des commandes :") 
        print("~ hello : L'ordinateur vous salue.")
        print("~ quit : Permet de quitter le programme, l'ordinateur vous dit aurevoir")
        print("~ settings : Pour modifier un paramètre")
        print("~ info : information sur la langue, le nom et le message affiché")
        print("~ help : permet d'ouvrir d'afficher les commandes \n")
    elif lan == "ES":
        print(">>> Lista de comandos :")
        print("~ hello : la computadora te saluda")
        print("~ quit : sale del programa, la computadora se despide")
        print("~ settings : para cambiar la configuración")
        print("~ info : información sobre el idioma, el nombre y el mensaje mostrado")
        print("~ help : muestra la lista de commandos \n")
    return 

## fonction info 
def info(langue,nom,prompt):
    """
    The function info() takes three arguments: langue, nom, and prompt. 
    It prints out a message in the language specified by langue, 
    using the name specified by nom, and the prompt specified by prompt.
    
    Args:
      langue: The language you want to use.
      nom: The name of the user.
      prompt: This is the text that is displayed to the user.
    
    Returns:
      the value of the variable "prompt"
    """
    if langue == "FR":
        print(">> Informations :")
        print("~ Langue : " + langue)
        print("~ Nom : " + nom)
        print("~ Message affiché : " + prompt)
    elif langue == "EN":
        print(">> Info :")
        print("~ Language : " + langue)
        print("~ Name : " + nom)
        print("~ Prompt : " + prompt)
    elif langue == "ES":
        print(">> Información :")
        print("~ Idioma : " + langue)
        print("~ Nombre : " + nom)
        print("~ Mensaje mostrado : " + prompt)
    return

