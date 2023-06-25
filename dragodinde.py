class Monture:
    def __init__(self, gender, reproductions, race, father=None, mother=None):
        self.gender = gender
        self.reproductions = reproductions
        self.race = race
        self.father = father
        self.mother = mother

        if self.gender == "Female" or self.gender == 'F':
            self.gestation = race.gestation


class Dragodinde(Monture):
    def __init__(self, gender, reproductions, race, father=None, mother=None):
        super().__init__(gender, reproductions, race, father, mother)
