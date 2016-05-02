__author__ = 'mbardoe'
import random
import VotingProfile
import cPickle as pickle
import Ballot, Election
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
        votingPref = self.VotingPreference.modifyPrefForRace(race)
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
        ## make sure that voters stay
        self.__save__()

    def populationSize(self):
        return len(self.population)

    def createElection(self):
        e = Election.Election(self.candidates)
        for person in self.population:
            ## determine if they want to vote
            if random.random() < person.VotingProb:
                ## they are voting
                ballot = Ballot.Ballot(
                    self.candidates[person.vote()], self, person.age, person.race, person.Immigrant
                )
                e.addBallot(ballot)
        return e

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
        races = ['White', 'African American', 'Hispanic', 'Asian', 'Other']
        return races[current]

    def __save__(self):
        pickle.dump(self, open(self.name + ".rgn", "wb"))


def main():

    ##vp=VotingProfile.VotingProfile([c,d], [.3,.7], [.1, .2], [.4,.6],[.1, .1], .2)
    ##print vp.__reNorm__([1,2,3])
    reg = pickle.load(open('Region_1.rgn', "rb"))

    # voter = reg.create_Voter()
    # print voter
    # print reg.candidates[voter.vote()]
    reg.create_Population(3000)
    e = reg.createElection()
    #print (e)
    e.candidateCount()
    print('\n\n')
    e.raceByCandidate()
    print (reg.populationSize())
    print('\n\n')
    e.raceByAge()


if __name__ == '__main__':
    main()