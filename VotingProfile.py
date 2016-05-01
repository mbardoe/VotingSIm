import random
import Candidate
import cPickle as pickle

class VotingProfile(object):

    def __init__(self, candidates, votingPrefAvg, votingPrefStdDev, SpectrumAvg, SpectrumStdDev,
                 ImmigrantProb, ImmigrantPref):
        if len(candidates)!=len(votingPrefAvg) or len(votingPrefAvg)!=len(votingPrefStdDev):
            raise SyntaxError("lengths don't match")
        self.candidates=candidates
        self.votingPrefAvg = votingPrefAvg
        self.votingPrefStdDev = votingPrefStdDev
        self.spectrumAvg=SpectrumAvg
        self.spectrumStdDev=SpectrumStdDev

    def createIndividualPref(self):
        indPref=[]
        ## determine individual preferences based on region
        for i in range(len(self.candidates)):
            indPref.append(min(max(random.gauss(self.votingPrefAvg[i],self.votingPrefStdDev[i]),0),1))
        indPref= self.__reNorm__(indPref)
        self.individualPreferences=indPref

        ## determine the spectrum Value of this voter
        for candidate in self.candidates:
            voterSpectrum=self.__cap__(random.gauss(self.spectrumAvg, self.spectrumStdDev))
        for i in range(len(self.candidates)):
            indPref[i]=indPref[i]/abs(candidate[i].spectrumValue-voterSpectrum)
        indPref= self.__reNorm__(indPref)
        self.individualPreferences=indPref
        return indPref

    def __reNorm__(self, mylist):
        mySum=float(sum(mylist))
        for i in range(len(mylist)):
            mylist[i]/=mySum
        return mylist

    def  __cap__(self, num):
        return min(max(num,0.0),1.0)



def main():
    c=Candidate.Candidate("Trump", .7)
    d=Candidate.Candidate("Hilary", .4)


    vp=VotingProfile([c,d], [.3,.7], [.1, .2], [.4,.6],[.1, .1], .2)
    print vp.__reNorm__([1,2,3])


if __name__=='__main__':
    main()