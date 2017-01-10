class Superhero(object):
    """
    Superhero
    --------------
    a class used to create super-powered beings, as opposed to augmented humans
    takes as arguments:
        name -> the hero name
        default abilities -> a SET 
    """

    def __init__(self, name):
        self.abilities = set()
        self.name = name
        self.gender = ""
        self.super_friends = set()
        self.evil_enemies = set()
        self.sidekicks = set()
        self.weaknesses = set()
        self.lair = ""
        self.biological_parents = tuple()

    def fight(self):
        pass

    def get_powers(self):
        return self.abilities

    def set_powers(self, new_abilities):
        self.abilities = new_abilities

    def add_power(self, new_ability):
        self.abilities.add(new_ability)

    def remove_power(self, ability_to_remove):
        self.abilities.remove(ability_to_remove)

    def __str__(self):
        power_output = ""
        for power in self.get_powers():
            power_output += power + ", "
        return "The superhero, {0} has the powers of {1}".format(self.name, power_output[:-2])
