# Exercice 2 Soit le fichier créé précédemment, écrire un programme qui copie le 
# contenu du fichier dans un autre fichier nommé copie-nomDuPremierFichier tout en mettant tout son contenu en majuscule


folder_name=input("Entrer le nom du fichier:\n")
folder_name_txt = (folder_name+".txt")
with open(folder_name_txt,'r') as f:
    contenu= f.read()
    contenu_maj=contenu.upper()
    with open('copie-nomDuPremierFichier.txt','a') as f2:
        contenu_final=f2.write(contenu_maj)





