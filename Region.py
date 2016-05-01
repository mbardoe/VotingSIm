__author__ = 'mbardoe'
import random
import VotingProfile
import cPickle as pickle
import Candidate


class Region(object):

    def __init__(self, Name, populationSize, raceBreakdown, AgeAvg, AgeStdDev, VotingAvg, VotingStdDev,
                 candidates, VotingPrefAvg, VotingPrefStdDev, SpectrumAvg, SpectrumStdDev,
                 ImmigrantProb, ImmigrantPref):
        self.name = Name
        self.AgeAvg = AgeAvg
        self.AgeStdDev = AgeStdDev
        self.VotingAvg = VotingAvg
        self.VotingStdDev = VotingStdDev
        self.VotingPreference = VotingProfile.VotingProfile(candidates,VotingPrefAvg, VotingPrefStdDev,
                                                            SpectrumAvg, SpectrumStdDev,
                                                            ImmigrantProb, ImmigrantPref)
        self.VotingPrefAvg = VotingPrefAvg
        self.VotingPrefStdDev = VotingPrefStdDev
        self.SpectrumAvg = SpectrumAvg
        self.SpectrumStdDev = SpectrumStdDev
        self.ImmigrantProb = ImmigrantProb
        self.populationSize=populationSize
        self.population=[]
        ## races are listed white, black, hispanic, asian, other
        self.raceBreakdown=self.__reNorm__(raceBreakdown)


    def create_Voter(self):
        age=self.__createAge__()
        voting = min(max(random.gauss(self.VotingAvg, self.VotingStdDev),0.0),1.0)
        myVotingPref=[]


    def __createAge__(self):
        ##num=random.gauss(45,8)**3

        ##num=int(num/2200.0-5.0)
        num=random.gauss(self.AgeAvg, self.AgeStdDev)**3
        num=int(num/self.AgeAvg**2-self.AgeStdDev)
        num=min(max(num,18), 100)
        return num

    def create_Population(self):
        pass

    def __reNorm__(self, mylist):
        mySum=float(sum(mylist))
        for i in range(len(mylist)):
            mylist[i]/=mySum
        return mylist

def main():
    c=Candidate.Candidate("Trump", .7)
    d=Candidate.Candidate("Hilary", .4)


    vp=VotingProfile.VotingProfile([c,d], [.3,.7], [.1, .2], [.4,.6],[.1, .1], .2)
    ##print vp.__reNorm__([1,2,3])


if __name__=='__main__':
