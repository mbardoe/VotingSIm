__author__ = 'mbardoe'
import random
import cPickle as pickle

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






