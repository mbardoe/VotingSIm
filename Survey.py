__author__ = "mbardoe@gmail.com"
import random
import Election, Ballot
import cPickle as pickle
import csv


class Survey(object):
    def __init__(self, candidates):
        self.type = None
        self.size = None
        self.bias = []
        self.region = None
        self.candidates = candidates
        self.CompleteSurvey = None

    def setRegion(self, region):
        self.region = region

    def simpleRandomSample(self, sampleSize, likelyVoters=False):
        self.type = "SRS"
        self.size = sampleSize
        if likelyVoters:
            self.sample = []
            while len(self.sample) < sampleSize:
                voter = random.choice(self.region.population)
                if voter.likelyVoter():
                    self.sample.append(voter)
        else:
            self.sample = random.sample(self.region.population, self.size)

    def stratifiedRandomSampleByRace(self, listOfTotalsByRace, likelyVoters=False):
        self.type = "Stratified"
        races = ["White", "African American", "Hispanic", "Asian", "Other"]
        result = {}
        self.sample = []
        for index in range(len(races)):
            race = races[index]
            result[race] = []
            while len(result[race]) < listOfTotalsByRace[index]:
                voter = random.choice(self.region.population)
                if (not likelyVoters) or voter.likelyVoter():
                    if voter.race == race:
                        result[race].append(voter)
                        self.sample.append(voter)
        self.sampleByRace = result

    def sortSampleByRace(self):
        self.sampleByRace = {}
        races = ["White", "African American", "Hispanic", "Asian", "Other"]
        for race in races:
            self.sampleByRace[race] = []
        for voter in self.sample:
            self.sampleByRace[voter.race].append(voter)

    def sortSampleByImmigrant(self):
        self.sampleByImmigrant = {}
        self.sampleByImmigrant["Immigrant"] = []
        self.sampleByImmigrant["Non-Immigrant"] = []
        for voter in self.sample:
            if voter.Immigrant:
                self.sampleByImmigrant["Immigrant"].append(voter)
            else:
                self.sampleByImmigrant["Non-Immigrant"].append(voter)


    def sortSampleByAge(self):
        self.type = "Stratified"
        self.sampleByAge = {}
        ages = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
        results = {}
        for age in ages:
            results[age] = []

        for voter in self.sample:
            newAge = (voter.age / 10 + 1) * 10
            results[newAge].append(voter)
        self.sampleByAge = results

    def stratifiedRandomSampleByAge(self, listofTotalsbyAge, likelyVoters=False):
        ages = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
        result = {}
        self.sample = []
        for index in range(len(ages)):
            age = ages[index]
            result[age] = []
            while len(result[age]) < listofTotalsbyAge[index]:
                voter = random.choice(self.region.population)
                newAge = (voter.age / 10 + 1) * 10
                if (not likelyVoters) or voter.likelyVoter():
                    if newAge == age:
                        result[age].append(voter)
                        self.sample.append(voter)
        self.sampleByAge = result

    def ASHAstratifiedRandomSampleByAge(self, listofTotalsbyAge, likelyVoters=False):
        ages = [(0, 46), (45, 110)]
        result = {}
        self.sample = []
        for index in range(len(ages)):
            age = ages[index]
            result[age] = []
            while len(result[age]) < listofTotalsbyAge[index]:
                voter = random.choice(self.region.population)
                #newAge = (voter.age / 10 + 1) * 10
                if (not likelyVoters) or voter.likelyVoter():
                    #if newAge==age:
                    if voter.age > age[0] and voter.age < age[1]:
                        result[age].append(voter)
                        self.sample.append(voter)

    def survey(self, voters):
        e = Election.Election(self.candidates)
        for person in voters:
            ## determine if they want to vote
            ##if random.random() < person.VotingProb: ## Should have made them decide between phone and in person
            ## they are voting
            ballot = Ballot.Ballot(
                self.candidates[person.vote()], self.region, person.age, person.race, person.Immigrant,
                person.VotingProb
            )
            e.addBallot(ballot)
        self.CompleteSurvey = e
        return e

    def createReportbyCandidate(self, voters):
        e = self.survey(voters)
        print e

    def createCSVReportbyCandidate(self, voters):
        e = self.survey(voters)
        return e.csvPrint()

    def createReportbyCandidateAndRace(self):
        races = ["White", "African American", "Hispanic", "Asian", "Other"]

        for race in races:
            print (race + "\n\n")
            voters = self.sampleByRace[race]
            e = self.survey(voters)
            print e

    def createCSVReportbyCandidateAndRace(self):
        races = ["White", "African American", "Hispanic", "Asian", "Other"]
        output = []
        for race in races:
            output.append([])
            output.append([race])
            voters = self.sampleByRace[race]
            e = self.survey(voters)
            output += e.csvPrint()
        return output


    def createReportbyCandidateAndAge(self):
        ages = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
        for age in ages:
            print (str(age) + "\n\n")
            voters = self.sampleByAge[age]
            e = self.survey(voters)
            print e

    def createCSVReportbyCandidateAndAge(self):
        ages = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
        output = []
        for age in ages:
            output.append([])
            output.append([str(age)])
            voters = self.sampleByAge[age]
            e = self.survey(voters)
            output += e.csvPrint()
        return output

    def createReportbyCandidateAndImmigrantStatus(self):
        statuses = ["Immigrant", "Non-Immigrant"]
        for status in statuses:
            print (status + "\n\n")
            voters = self.sampleByImmigrant[status]
            e = self.survey(voters)
            print e

    def createCSVReportbyCandidateAndImmigrantStatus(self):
        statuses = ["Immigrant", "Non-Immigrant"]
        output = []
        for status in statuses:
            output.append([])
            output.append([status])
            voters = self.sampleByImmigrant[status]
            e = self.survey(voters)
            output += e.csvPrint()
        return output

    def createReportbyCandidateAndRegion(self):
        pass

    def createReport(self):
        self.sortSampleByAge()
        self.sortSampleByImmigrant()
        self.sortSampleByRace()
        self.createReportbyCandidate(self.sample)
        print("\n\n\n")
        self.createReportbyCandidateAndRace()
        print("\n\n\n")
        self.createReportbyCandidateAndAge()
        print("\n\n\n")
        self.createReportbyCandidateAndImmigrantStatus()

    def createCSVReport(self, filename):
        self.sortSampleByAge()
        self.sortSampleByImmigrant()
        self.sortSampleByRace()
        with open(filename, 'w') as csvfile:
            a = csv.writer(csvfile, delimiter=",")
            a.writerows(self.createCSVReportbyCandidate(self.sample))
            a.writerows(self.createCSVReportbyCandidateAndRace())
            a.writerows(self.createCSVReportbyCandidateAndAge())
            a.writerows(self.createCSVReportbyCandidateAndImmigrantStatus())


    def createVoterCSV(self, filename):
        with open(filename, 'w') as csvfile:
            a = csv.writer(csvfile, delimiter=",")
            a.writerow(self.CompleteSurvey.ballots[0].header())
            for ballot in self.CompleteSurvey.ballots:
                a.writerow(ballot.row())


def main():
    ##vp=VotingProfile.VotingProfile([c,d], [.3,.7], [.1, .2], [.4,.6],[.1, .1], .2)
    ##print vp.__reNorm__([1,2,3])
    for i in [1, 2, 3, 4]:
        reg = pickle.load(open('Region_' + str(i) + '.rgn', "rb"))

        # voter = reg.create_Voter()
        # print voter
        # print reg.candidates[voter.vote()]
        #reg.create_Population(40000)
        survey = Survey(reg.candidates)
        survey.setRegion(reg)
        survey.simpleRandomSample(500)
        #survey.ASHAstratifiedRandomSampleByAge([250,250])
        survey.createReport()
        #survey.createReportbyCandidate(survey.sample)
        #survey.stratifiedRandomSampleByRace([200,75,75,75,75])
        #survey.createReport()
        survey.createVoterCSV("JRsurveyReg" + str(i) + "Voters.csv")
        #print(survey.createCSVReportbyCandidate(survey.sample))
        #print(survey.createCSVReportbyCandidateAndRace())
        survey.createCSVReport("JRsurveyReg" + str(i) + "Results.csv")
        #print survey.sample
        #survey.createReportbyCandidateAndRace()
        #survey.survey(survey.sample)
        #survey.createReportbyCandidate()


if __name__ == '__main__':
    main()
