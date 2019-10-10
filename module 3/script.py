import logging

NOMS = ['Alice', 'Bob', 'Charlie']
IDs = [1, 2, 3]

class Fiche:

    def __init__(self, id, nom):
        self._id = id
        self._nom = nom

    def __repr__(self):
        return '{}: {}'.format(self._id, self._nom)

def genere():
    salaries = []
    for i in IDs:
        logging.info("Creation d'un nouveau salarié")
        salaries.append(Fiche(i, NOMS[i]))
    print(salaries)

if __name__ == "__main__":
    genere()
