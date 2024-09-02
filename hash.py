import hashlib
import os
import requests

hash_algorithme=input('Donnez le hash que vous voulez')
file_name = input('Donnez le nom du fichier à analyser')
fichier_chemin= os.path.join(os.getcwd(), file_name)
url=input("Donner l'url du site officiel")

"""Calcule le hash d'un fichier donné"""

def calculate_hash(file_path, hash_algorithme):
    hash_fonc=hashlib.new(hash_algorithme)
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda:f.read(4096), b""):
                hash_fonc.update(chunk)
    except FileNotFoundError:
        print(f"Le fichier n'est pas trouvé")
        return None
    except IOError as e:
        print(f"Erreur d'entrée/sortie: {e}")
        return None
    return hash_fonc.hexdigest()


"""Calcul le hash d'un fichier issu du site officiel"""
def get_official_hash(url):
    try:
        reponse=requests.get(url)
        hash_officiel= hashlib.new(hash_algorithme)
        for chunk in reponse.iter_content(4096):
            if chunk:
                hash_officiel.update(chunk)
    except requests.RequestException as e:
        print(f"Erreur lors du téléchargement du hash {e}")
        return None
    return hash_officiel.hexdigest()


fichier_hash = calculate_hash(fichier_chemin, hash_algorithme)
officiel_hash= get_official_hash(url)

if fichier_hash:
    print(f"Le hash de ce fichier est {fichier_hash}")
    
if officiel_hash:
    print(f"Le hash du site officiel est: {officiel_hash}")

"""Comparaison du fichier téléchargé et celle du fichier issu du site officiel"""

if fichier_hash == officiel_hash:
    print('Fiable')
else:
    print('Corrompu, à ne pas ouvrir')    


