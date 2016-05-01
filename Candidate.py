__author__ = 'mbardoe'

class Candidate(object):
    MYID=0

    def __init__(self, name, spectrumValue, racePref):
        self.name = name  ## a name to identify the candidate with
        self.myID = Candidate.MYID  ## an ID to identify candidates with
        Candidate.MYID+=1
        ## spectrumValue is where a candidate is on the liberal (0) to conservative scales (1)
        self.spectrumValue = spectrumValue  ## a float to identify where a candidate fits on the liberal conserv spectrum
        self.racePref = racePref

    def __str__(self):
        return self.name;


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
    c = Candidate("Trump", .7, trumpRace)
    d = Candidate("Hilary", .4, HillRace)
    print str(c.myID)+' '+c.name
    print str(d.myID)+' '+d.name

if __name__=='__main__':
    main()
