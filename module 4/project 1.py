# Dans ce projet, vous allez mettre en place un jeu de test pour le programme de purge

import pytest

# liste de fichiers de test à générer ou copier
DUMMY_FILES = [...]

@pytest.fixture()
def test_folder():
    # Créer un répertoire de test, créer des fichiers dans ce répertoire de test, certains plus anciens que 10 jours, d'autres plus récent
    (...)
    yield folder

    # Détruire le répertoire de test et tout ce qu'il contient en fin de test

# Les fonctions préfixées par test_ seront exécutées automatiquement par le moteur de test
def test_list_files():
    my_folder = test_folder

    (...)

    assert (...)

def test_compress_file():
    my_folder = test_folder

    (...)

    assert (...)

def test_purge_folder():
    my_folder = test_folder

    (...)

    assert (...)
