# class Musician:
#     def __init__ (self,)
#     pass

# class Guitarist(Musician):
#     pass

from abc import abstractmethod


class Band:
    bands_arr = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.bands_arr.append(self.members)

    def play_solos(self):

        return ["face melting guitar solo", "bom bom buh bom", "bom bom buh bom"]

    @classmethod
    def to_list(cls):
        return cls.bands_arr


class Musician:
    def __init__(self, name):
        self.name = name


class Guitarist(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return 'face melting guitar solo'


class Drummer(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'rattle boom crash'


class Bassist(Musician):

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'