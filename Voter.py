__author__ = 'mbardoe'
import random
import cPickle as pickle
import Region
import Candidate
import VotingProfile


class Voter(object):
    ID_Num=1
    def __init__(self, region, race, age, VotingProb, PhoneProb, PersonProb, VotingPref, Spectrum, Immigrant):
        self.region = region
        self.ID = Voter.ID_Num
        Voter.ID_Num+=1
        self.race=race
        self.age=age
        self.VotingProb = VotingProb
        self.PhonePref = PhoneProb
        self.PersonProb= PersonProb
        self.VotingPref = VotingPref
        self.Spectrum = Spectrum
        self.Immigrant= Immigrant

    def surveyRespond(self,type):
        if type=="phone":
            return random.random()<self.PhonePref

        if type=="in Person":
            return random.random()<self.PersonProb

    def voteRespond(self):
        return random.random()<self.VotingProb

    def vote(self):
        vote=random.random()
        current=0
        testProb=self.VotingPref[current]
        while vote>testProb:
            vote-=testProb
            current+=1
            testProb=self.VotingPref[current]
        return current

    def likelyVoter(self):
        return self.VotingProb>.7

    def __str__(self):
        val = "Region: " + str(self.region.name) + "\n"
        val += "ID: " + str(self.ID) + "\n"
        val += "age: " + str(self.age) + "\n"
        val += "race: " + str(self.race) + "\n"
        val += "Voting Probability: " + str(self.VotingProb) + "\n"
        val += "Voting Preferences: " + str(self.VotingPref) + "\n"
        val += "Spectrum: " + str(self.Spectrum) + "\n"
        val += "Immigrant: " + str(self.Immigrant) + "\n"
        return val


def main():
    trumpRace = {'white': .5,
                 'African American': 0.01,
                 'Hispanic': 0.01,
                 'Asian': 0.1,
                 'Other': 0.2}
    HillRace = {'white': .2,
                'African American': 0.5,
                'Hispanic': 0.5,
                'Asian': 0.1,
                'Other': 0.2}
    c = Candidate.Candidate("Trump", .7, trumpRace)
    d = Candidate.Candidate("Hilary", .4, HillRace)
    ##vp=VotingProfile.VotingProfile([c,d], [.3,.7], [.1, .2], [.4,.6],[.1, .1], .2)
    ##print vp.__reNorm__([1,2,3])
    reg = Region.Region("Region 1", 30, [.3, .3, .2, .1, .1], 45.0, 8.0, .5, .05,
                        [c, d], [.3, .7], [.1, .1], [.4, .6], [.1, .1],
                        .2, [.8, .2])
    voter = Voter(reg, "white", 45, .8, .5, .6, [.3, .7], .8, False)
    print voter
    print (str(voter.vote()))
    print (str(voter.likelyVoter()))


if __name__ == '__main__':
    main()









