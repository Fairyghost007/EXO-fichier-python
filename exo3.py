# Exercice 3 :
# Soit le fichier créé précédemment, 
# écrire un programme qui copie le contenu du fichier dans un autre fichier nommé copie-nomDuPremierFichier 
# tout en mettant un numéro d'ordre devant chaque fruit.






folder_name=input("Entrer le nom du fichier:\n")
folder_name_txt = (folder_name+".txt")
with open(folder_name_txt,'r') as f:
    lignes=f.readlines()
    print(lignes)
    numero=0
    for ligne in lignes:
        with open('copie-nomDuPremierFichier.txt','a') as f2:
            new_ligne=(numero,"."+ligne,"\n")
            new_ligne_final=f.write(new_ligne)
            numero+=1
            print(new_ligne)



