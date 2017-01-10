import unittest
from superman import *

class TestSuperman(unittest.TestCase):

    @class

    def test_SupermanMustBeASuperhero(self):
        superman = Superman()
        self.assertIsInstance(superman, Superhero, "superman is a superhero")

    def test_SupermanMustBeAFliyingSuperhero(self):
        superman = Superman()
        self.assertIsInstance(superman, Flight, "superman is NOT a Flight!!")

    def test_SupermanMustBeARunningSuperhero(self):
        superman = Superman()
        self.assertIsInstance(superman, Running, "superman is NOT a Running!!")

    def test_SupermanMustBeASwimmingSuperhero(self):
        superman = Superman()
        self.assertIsInstance(superman, Swimming, "superman is NOT a swimming!!")

    def test_SupermanMustFlyAtOurSpeed(self):
        superman = Superman()
        self.assertEqual(superman.airspeed, 1000000)

    def test_SupermanMustSwimAtOurSpeed(self):
        superman = Superman()
        self.assertEqual(superman.water_speed, 250)
    
    def test_SupermanMustBeBulletproof(self):
        superman = Superman()
        self.assertTrue(superman.is_bulletproof)


if __name__ == '__main__':
    unittest.main()