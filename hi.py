import os
import datetime

i=0
# Chemin d'accès du dossier à créer
"""new_directory_path = r'Bureau\lll'
def concatin(a,b):
    z=str(a)+str(b)
    return(z)

def path(x):
    path="r"+str(x)
    
# Vérifier si le dossier existe déjà
if not os.path.exists(new_directory_path):
    # Créer le dossier
    os.makedirs(new_directory_path)
    print(f'Le dossier {new_directory_path} a été créé avec succès.')
else:
    heure_actuelle = str(datetime.datetime.now().time())

    chemin = r'Bureau\lll\ll.txt'
    with open(chemin, mode='w') as fichier:
        pass
    print(f'Le dossier {new_directory_path} existe déjà, il est recréé')"""

s = datetime.datetime.now()
p=s.strftime("%Y-%m-%d %H:%M:%S")
print(p)