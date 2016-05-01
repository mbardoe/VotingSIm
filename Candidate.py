__author__ = 'mbardoe'

class Candidate(object):
    MYID=0

    def __init__(self, name, spectrumValue):
        self.name=name
        self.myID=Candidate.MYID
        Candidate.MYID+=1
        ## spectrumValue is where a candidate is on the liberal (0) to conservative scales (1)
        self.spectrumValue=spectrumValue

def main():
    c=Candidate("Trump", .7)
    d=Candidate("Hilary", .4)
    print str(c.myID)+' '+c.name
    print str(d.myID)+' '+d.name

if __name__=='__main__':
    main()
