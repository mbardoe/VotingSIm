__author__ = 'mbardoe'


class Election(object):
    def __init__(self, candidates):
        self.ballots = []
        self.candidates = candidates


    def addBallot(self, ballot):
        self.ballots.append(ballot)

    def candidateCount(self):
        results = {}
        numVotes = float(len(self.ballots))
        for candidate in self.candidates:
            results[candidate.name] = 0
        for ballot in self.ballots:
            results[ballot.candidate.name] += 1
        for result in results.keys():
            print(result + ":  " + str(results[result]) + "  " + str(results[result] / numVotes))
        print numVotes
        return results


    def raceCount(self, ballots):
        races = ['White', 'African American', 'Hispanic', 'Asian', 'Other']
        results = {}
        for race in races:
            results[race] = 0
        for ballot in ballots:
            results[ballot.race] += 1
        for result in results.keys():
            print(result + ":  " + str(results[result]))
        return results

    def ageCount(self, ballots):
        ages = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
        results = {}
        for age in ages:
            results[age] = 0
        for ballot in ballots:
            newAge = (ballot.age / 10 + 1) * 10
            results[newAge] += 1
        for result in results.keys():
            print(str(result) + "\'s:  " + str(results[result]))
        return results

    def ballotsForCandidate(self, candidate):
        result = []
        for ballot in self.ballots:
            if ballot.candidate == candidate:
                result.append(ballot)
        return result

    def raceByCandidate(self):
        for candidate in self.candidates:
            print (candidate.name + "\n")
            theirBallots = self.ballotsForCandidate(candidate)
            self.raceCount(theirBallots)

    def raceByAge(self):
        for candidate in self.candidates:
            print (candidate.name + "\n")
            theirBallots = self.ballotsForCandidate(candidate)
            self.ageCount(theirBallots)

    def __str__(self):
        results = self.candidateCount()
        output = ""
        for candidate in results.keys():
            output += candidate + ":  " + str(results[candidate]) + "\n"
        return output


