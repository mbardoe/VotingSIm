__author__ = 'mbardoe'


class Ballot(object):
    def __init__(self, candidate, region, age, race, immigrant):
        self.candidate = candidate
        self.region = region
        self.age = age
        self.race = race
        self.immigrant = immigrant
