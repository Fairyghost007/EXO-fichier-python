# Soit une liste d'éléments, écrire un programme qui transfère le contenu de la liste dans un fichier txt dont le nom sera saisi par l’utilisateur.

liste_fruits=["mangue", "pomme", "papaye", "banane", "coco"]
folder_name=input("Entrer le nom du fichier:\n")
folder_name_txt = (folder_name+".txt")
for i in liste_fruits:
    with open(folder_name_txt,'a') as f:
        add_fruit=f.write(i +"\n")












