__author__ = 'mbardoe'
import random
import VotingProfile
import cPickle as pickle
import Candidate
import Voter


class Region(object):
    def __init__(self, Name, raceBreakdown, AgeAvg, AgeStdDev, VotingAvg, VotingStdDev,
                 candidates, VotingPrefAvg, VotingPrefStdDev, SpectrumAvg, SpectrumStdDev,
                 ImmigrantProb, ImmigrantPref):
        self.name = Name  ## a string representing the region
        self.AgeAvg = AgeAvg  ## the average age of a voter
        self.AgeStdDev = AgeStdDev  ## the variation in ages
        self.VotingAvg = VotingAvg  ## average chance a voter votes
        self.VotingStdDev = VotingStdDev  ## variation in the voting probability
        ## a tool to create voting preferences
        self.VotingPreference = VotingProfile.VotingProfile(candidates,VotingPrefAvg, VotingPrefStdDev,
                                                            SpectrumAvg, SpectrumStdDev,
                                                            ImmigrantProb, ImmigrantPref)

        self.population = []  ## population
        self.phoneProbAvg = .5  ## average probability voter can be reached by phone
        self.phoneProbStdDev = .1  ## variation in probability that voter can be reached by phone
        self.PersonProbAvg = .7  ## average probability you can reach a voter in person
        self.PersonProbStdDev = .1  ## average variation in the probability you can reach them in person
        ## races are listed White, African American, Hispanic, Asian, Other
        self.raceBreakdown = self.__reNorm__(raceBreakdown)  ## breakdown of the region by race
        self.candidates = candidates  ## list of candidates
        self.ImmigrantProb = ImmigrantProb


    def create_Voter(self):
        age=self.__createAge__()
        voting = min(max(random.gauss(self.VotingAvg, self.VotingStdDev),0.0),1.0)
        myVotingPref=[]
        race = self.determineRace()
        phoneProb = self.__cap__(random.gauss(self.phoneProbAvg, self.phoneProbStdDev))
        personProb = self.__cap__(random.gauss(self.PersonProbAvg, self.PersonProbStdDev))
        spectrum = self.VotingPreference.voterSpectrum()
        immigrant = (random.random() < self.ImmigrantProb)
        votingPref = self.VotingPreference.createIndividualPref()
        votingPref = self.VotingPreference.modifyPrefForSpectrum(spectrum)
        votingPref.self.VotingPreference.modifyPrefForRace(race)
        if immigrant:
            votingPref = self.VotingPreference.modifyPrefForImmigrants()

        voter = Voter.Voter(self, race, age, voting, phoneProb, personProb, votingPref, spectrum, immigrant)
        return voter


    def __createAge__(self):
        ##num=random.gauss(45,8)**3

        ##num=int(num/2200.0-5.0)
        num=random.gauss(self.AgeAvg, self.AgeStdDev)**3
        num=int(num/self.AgeAvg**2-self.AgeStdDev)
        num=min(max(num,18), 100)
        return num

    def create_Population(self, n):
        """ Add n voters to the population"""
        for i in range(n):
            self.population.append(self.create_Voter())

    def __reNorm__(self, mylist):
        mySum=float(sum(mylist))
        for i in range(len(mylist)):
            mylist[i]/=mySum
        return mylist

    def __cap__(self, num, myMin=0.0, myMax=1.0):
        """Keep values between 0 and 1"""
        return min(max(num, myMin), myMax)

    def determineRace(self):
        race = random.random()
        current = 0
        testProb = self.raceBreakdown[current]
        while race > testProb:
            race -= testProb
            current += 1
            testProb = self.raceBreakdown[current]
        races = ['White', 'African-American', 'Hispanic', 'Asian', 'Other']
        return races[current]


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
    reg = Region("Region 1", 30, [.3, .3, .2, .1, .1], 45.0, 8.0, .5, .05,
                 [c, d], [.3, .7], [.1, .1], .4, .1,
                 .2, [.8, .2])

    voter = reg.create_Voter()
    print voter
    print reg.candidates[voter.vote()]


if __name__ == '__main__':
    main()