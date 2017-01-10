class Flight(object):

    def __init__(self):
        self.airspeed = 0
        self.max_load = 0
        self.max_altitude = 0

    def fly(self):
        print("I'm flying at {} mps!".format(self.airspeed))
        pass
