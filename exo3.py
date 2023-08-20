# Exercice 3 :
# Soit le fichier créé précédemment, 
# écrire un programme qui copie le contenu du fichier dans un autre fichier nommé copie-nomDuPremierFichier 
# tout en mettant un numéro d'ordre devant chaque fruit.






folder_name=input("Entrer le nom du fichier:\n")
folder_name_txt = (folder_name+".txt")
with open('exo-fichier-python/'+folder_name_txt,'r') as f:
    numero=0
    for ligne in f:
        with open('exo-fichier-python/copie-nomDuPremierFichier.txt','a') as f2:
            f2.write(str(numero) + ". ")
            f2.write(ligne)
            numero+=1



