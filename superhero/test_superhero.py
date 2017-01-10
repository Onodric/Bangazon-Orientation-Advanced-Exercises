import unittest
from superhero import *

class TestSuperhero(unittest.TestCase):

    def test_SuperheroMustHaveNameProperty(self):
        random_superhero = Superhero("Bilbo")
        self.assertEqual(random_superhero.name, "Bilbo")

    def test_SuperheroAddPowerMustAddPower(self):
        random_superhero = Superhero("Clark")
        random_superhero.add_power("RandomPower")
        self.assertIn("RandomPower", random_superhero.get_powers())

    def test_SuperheroRemovePowerMustRemovePower(self):
        random_superhero = Superhero("Shiggity")
        random_superhero.add_power("RandomPower1")
        random_superhero.add_power("RandomPower2")
        random_superhero.add_power("RandomPower3")
        random_superhero.remove_power("RandomPower2")
        self.assertNotIn("RandomPower2", random_superhero.get_powers())
        

if __name__ == '__main__':
    unittest.main()

