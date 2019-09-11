# Installation de l'environement

### Télécharger Anaconda
https://www.anaconda.com/distribution/#download-section

### Télécharger PyCharm
Choisir la version "community" :
https://www.jetbrains.com/pycharm/download/#section=windows

### Télécharger Git
https://git-scm.com/download/win

### Lancer PyCharm et importer les cours
Dans PyCharm, ouvrir le menu "VCS", "Checkout from version control", "Git", puis utiliser l'url suivante : 
https://github.com/lbadouin/CoursPython.git


Alternativement, aller à https://github.com/lbadouin/CoursPython, puis choisissez "Clone or Download" puis "Download Zip"

### Lancer Jupyter
Lancer "Anaconda Prompt", aller dans le répertoire du projet de cours, puis lancer la commande "jupyter notebook"


## Optionnel : Parametrer un environement virtuel et un noyau jupyter

Un environement virtuel permet de créer un espace de travail isolé sur une machine. Celà permet par exemple de s'assurer que votre code ne fait pas appel à des modules qui ne seront pas présent sur votre environement cible, ou encore travailler avec plusieurs versions de python.
Un noyeau jupyter permet d'exécuter un notebook en se basant sur un environement virtuel.

* Lancer "Anaconda prompt"
* Aller dans le répertoire du projet
* taper la commande 'python -m venv cour_python' pour créer l'environement virtuel
* Activer l'environnement virtuel en lancant la commande 'activate' dans le répertoire script de votre environnement virtuel. La commande deactivate permet de quitter l'environement virtuel.
* Créer un kernel lié à l'environnement actif avec la commande 'ipython kernel install --user --name=cours_python'
* Lancer jupyter : vous pouvez à présent selectionner avec quel kernel vous souhaitez exécuter votre notebook
* Astuce : la commande "pip freeze" permet de récupérer la liste des modules présents dans l'environement courant.

