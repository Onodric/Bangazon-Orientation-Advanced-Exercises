from superhero import *
from sidekick import *
from flight import *
from swimming import *
from running import *
from bulletproof import *

class Superman(Superhero, Flight, Running, Swimming, Bulletproof):

    def __init__(self):
        Superhero.__init__(self, 'Superman')
        Bulletproof.__init__(self)
        self.add_power(Flight())
        self.add_power("Super Strength")
        self.add_power("Laser Vision")
        self.add_power("Bulletproof")
        self.airspeed = 1000000
        self.max_altitude = 200000000
        self.water_speed = 250


