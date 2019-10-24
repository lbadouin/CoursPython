# Exercice 1 : créer un module d'archivage de fichier.
# Ce module doit permettre de compresser des fichiers plus vieux que n jours.
# Utilisez le module logger pour tracer les opérations et la gestion d'exceptions pour protéger votre code

DELAY = 10

def list_old_files(folder, n=DELAY):
    # Renvoie la liste des fichiers du répertoire plus vieux que n jours
    pass

def compress_file(file):
    # Compresse un fichier et supprime le fichier original.
    # Le fichier compressé doit avoir la même date de modification que le fichier original
    # Vous pouvez découper ce code en sous fonctions
    pass

def archive_folder(folder, n=DELAY):
    # Compresse  tous les fichiers de ce répertoire plus vieux que n jounrs
    pass
