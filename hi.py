import os
import datetime


## function time now
def timez():
    s = datetime.datetime.now()
    p = s.strftime("d%H%M")
    return(p)
ee = "Bureau/lll"
##fonction concatination path
def pathz():
    s1=timez()

    z=str(ee)+str(s1)+".txt"
    return(str(z))

## Fonction path
def path(x):
    path=str(x)
    return(path)
i=0
# Chemin d'accès du dossier à créer
new_directory_path = r'Bureau/lll'
new_directory_path1 = path(ee)



def concatin(a,b):
    z=str(a)+str(b)
    return(z)


    
# Vérifier si le dossier existe déjà
if not os.path.exists(ee):
    # Créer le dossier
    os.makedirs(ee)
    print(f'Le dossier {new_directory_path} a été créé avec succès.')
else:


    chemin = r'Bureau/lll/ll.txt'
    with open(pathz(), mode='w') as fichier:
        pass
    print(f'Le dossier {new_directory_path1} existe déjà, il est recréé')
