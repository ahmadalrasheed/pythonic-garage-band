from abc import abstractmethod



class Band():
    """
    This class defines a band and its' members and allows them to play their instrument.
    name: str
    members: list
    """

    instances = []
    solo_list = []
    def __init__(self, name = "", members = []):
        self.name = str(name)
        self.members = list(members)
        Band.instances.append(self)

    def __str__(self):
        return (f"This band is called {self.name} and has {len(self.members)} members.")

    def __repr__(self):
        return (f"This band is called {self.name} and has {len(self.members)} members.")
    
    @abstractmethod
    def play_solos(cls):
        """
        This function calls band members to play their instruments.
        """

        return cls.solo_list
    
    @classmethod
    def to_list(cls):
        """
        This calls created bands.
        """
        return cls.instances






class Musician(Band):
    """
    This class defines the role of each band member.
    name: str
    role: str
    instrument: str
    sounds: str
    """

    def __init__(self, name = "", role = "", instrument = "", sounds = ""):
        self.name = str(name)
        self.role = str(role) 
        self.instrument = str(instrument)
        sounds = str(sounds)

    def __str__ (self):
        return (f"My name is {self.name} and I play {self.instrument}")

    def __repr__ (self):
        return (f"{self.role} instance. Name = {self.name}")

    def get_instrument(self):
        """
        This function specifies which instrument a band member uses.
        """
        return self.instrument

    def play_solo(self):
        """
        This tells band member to play their instrument.
        """
        Band.solo_list.append(self.sounds)
        return self.sounds



class Guitarist(Musician):
    """
    This class specifies Guitarist band memeber characteristics.
    """
    def __init__(self, name = ""):
        self.name = str(name)
        self.role = "Guitarist" 
        self.instrument = "guitar"
        self.sounds = "face melting guitar solo"

class Bassist(Musician):
    """
    This class specifies Bassist band memeber characteristics.
    """
    def __init__(self, name = ""):
        self.name = str(name)
        self.role = "Bassist" 
        self.instrument = "bass"
        self.sounds = "bom bom buh bom"


class Drummer(Musician):
    """
    This class specifies Drummer band memeber characteristics.
    """
    def __init__(self, name = ""):
        self.name = str(name)
        self.role = "Drummer" 
        self.instrument = "drums"
        self.sounds = "rattle boom crash"


if __name__ == "__main__":
    test_band = Band("test", ["a", "b", "c"])
    print(test_band.instances)
    # print(test_band.solo_list)

    # print(test_band.to_list())
    # test_band.sign_band()
    # print(bands)
    # testman = Guitarist("testman")
    # print(testman)