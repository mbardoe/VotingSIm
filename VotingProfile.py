import random
import Candidate
import cPickle as pickle


class VotingProfile(object):
    def __init__(self, candidates, votingPrefAvg, votingPrefStdDev, SpectrumAvg, SpectrumStdDev,
                 ImmigrantProb, ImmigrantPref):
        if len(candidates) != len(votingPrefAvg) or len(votingPrefAvg) != len(votingPrefStdDev):
            raise SyntaxError("lengths don't match")
        self.candidates = candidates
        self.votingPrefAvg = votingPrefAvg
        self.votingPrefStdDev = votingPrefStdDev
        self.spectrumAvg = SpectrumAvg
        self.spectrumStdDev = SpectrumStdDev
        self.immigrantProb = ImmigrantProb
        self.immigrantPref = ImmigrantPref

    def createIndividualPref(self):
        """This function creates individual voting preferences but does not apply
        the immigrant changes"""
        indPref = []
        ## determine individual preferences based on region
        for i in range(len(self.candidates)):
            indPref.append(min(max(random.gauss(self.votingPrefAvg[i], self.votingPrefStdDev[i]), 0), 1))
        indPref = self.__reNorm__(indPref)
        self.individualPreferences = indPref

    def voterSpectrum(self):
        """ determine the spectrum Value of this voter"""
        return self.__cap__(random.gauss(self.spectrumAvg, self.spectrumStdDev))

    def modifyPrefForSpectrum(self, voterSpectrum):
        """Apply the spectrum feelings"""
        indPref = self.individualPreferences
        for i in range(len(self.candidates)):
            indPref[i] = indPref[i] / abs(self.candidates[i].spectrumValue - voterSpectrum)
        indPref = self.__reNorm__(indPref)
        self.individualPreferences = indPref

        return indPref


    def modifyPrefForImmigrants(self):
        """Apply the immigrant feelings"""
        indPref = self.individualPreferences
        for i in range(len(self.candidates)):
            indPref[i] = indPref[i] * self.immigrantPref[i]
        indPref = self.__reNorm__(indPref)
        self.individualPreferences = indPref
        return indPref

    def modifyPrefForRace(self, race):
        indPref = self.individualPreferences
        for i in range(len(self.candidates)):
            indPref[i] *= self.candidates[i].racePref[race]
        indPref = self.__reNorm__(indPref)
        self.individualPreferences = indPref
        return indPref

    def __reNorm__(self, mylist):
        """Helper function to make a list of weights add to 1.0"""
        mySum = float(sum(mylist))
        for i in range(len(mylist)):
            mylist[i] /= mySum
        return mylist


    def __cap__(self, num, myMin=0.0, myMax=1.0):
        """Keep values between 0 and 1"""
        return min(max(num, myMin), myMax)


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

    vp = VotingProfile([c, d], [.3, .7], [.1, .2], .4, .1, .2, [.2, .8])
    print vp.__reNorm__([1, 2, 3])


if __name__ == '__main__':
    main()