from superman import *

if __name__ == "__main__":
    jimmy = Sidekick("Jimmy Olsen")

    superman = Superman()
    
    superman.sidekicks.add(jimmy)
    superman.add_power("Expanded-Spectrum Vision")
    superman.add_power("Cold Breath")
    
    # print(superman)
    # print(superman.get_powers())
    
    # print(dir(superman))
    for sidekick in superman.sidekicks:
        print(sidekick)
    superman.fly()