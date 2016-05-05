__author__ = 'mbardoe'


class Ballot(object):
    def __init__(self, candidate, region, age, race, immigrant, liklihood):
        self.candidate = candidate
        self.region = region
        self.age = age
        self.race = race
        self.immigrant = immigrant
        self.liklihoodOfVoting = liklihood

    def row(self):
        if self.immigrant:
            status = "Immigrant"
        else:
            status = "Non-immigrant"
        #print(str(self.region))
        return [str(self.candidate), str(self.region), str(self.age), str(self.race), status,
                str(self.liklihoodOfVoting)]

    def header(self):
        return ["Candidate Preference", "Region", "Age", "Race", "Immigrant", "Liklihood of Voting"]

