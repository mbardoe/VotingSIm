__author__ = 'mbardoe'
import Voter, Region, Candidate
import cPickle as pickle


class buildObjects(object):
    def __init__(self):
        self.candidates = ['Trump', 'Hillary', 'Cruz', 'Kasich', 'Sanders']
        self.regions = ['Region_1', 'Region_2', 'Region_3', 'Region_4', 'Region_5']


def main():
    trumpRace = {'White': .3,
                 'African American': 0.01,
                 'Hispanic': 0.01,
                 'Asian': 0.1,
                 'Other': 0.2}
    HillRace = {'White': .2,
                'African American': 0.35,
                'Hispanic': 0.35,
                'Asian': 0.1,
                'Other': 0.2}
    CruzRace = {'White': .3,
                'African American': 0.1,
                'Hispanic': 0.3,
                'Asian': 0.1,
                'Other': 0.2}
    KasichRace = {'White': .3,
                  'African American': 0.1,
                  'Hispanic': 0.1,
                  'Asian': 0.1,
                  'Other': 0.2}
    BernieRace = {'White': .3,
                  'African American': 0.2,
                  'Hispanic': 0.3,
                  'Asian': 0.3,
                  'Other': 0.3}
    c = Candidate.Candidate("Trump", .7, trumpRace)
    d = Candidate.Candidate("Hillary", .4, HillRace)
    e = Candidate.Candidate("Cruz", .8, CruzRace)
    f = Candidate.Candidate("Kasich", .55, KasichRace)
    g = Candidate.Candidate("Sanders", .2, BernieRace)
    candidates = [c, d, e, f, g]

    for candidate in candidates:
        pickle.dump(candidate, open(candidate.name + ".cand", "wb"))

    r1 = Region.Region("Region_1",
                       [.4, .2, .1, .1, .05],  ## race breakdown
                       50,  ## avg Age
                       10,  ## variation in age
                       .6,  ## prob voting
                       .1,  ## variation in voting
                       candidates,  ## candidates
                       [1.8, 1.8, .4, .1, .3],  ## candidate pref
                       [.4, .4, .2, .01, .07],  ## variation in candidate pref
                       .6,  # spectrum
                       .07,  # variation in spectrum
                       .03,  # immigrant prob
                       [.05, .4, .4, .2, .2])  ## immigrant pref)

    r2 = Region.Region("Region_2",
                       [.45, .3, .05, .1, .1],  ## race breakdown
                       40,  ## avg Age
                       7,  ## variation in age
                       .5,  ## prob voting
                       .1,  ## variation in voting
                       candidates,  ## candidates
                       [.3, .4, .4, .2, .6],  ## candidate pref
                       [.1, .1, .1, .1, .2],  ## variation in candidate pref
                       .4,  # spectrum
                       .15,  # variation in spectrum
                       .05,  # immigrant prob
                       [.05, .4, .4, .2, .2])  ## immigrant pref)
    r3 = Region.Region("Region_3",
                       [.7, .1, .1, .07, .03],  ## race breakdown
                       45,  ## avg Age
                       6,  ## variation in age
                       .54,  ## prob voting
                       .1,  ## variation in voting
                       candidates,  ## candidates
                       [1.2, .4, .4, .2, .5],  ## candidate pref
                       [.3, .1, .1, .05, .2],  ## variation in candidate pref
                       .8,  # spectrum
                       .2,  # variation in spectrum
                       .05,  # immigrant prob
                       [.05, .4, .4, .2, .2])  ## immigrant pref)
    r4 = Region.Region("Region_4",
                       [.1, .6, .1, .15, .05],  ## race breakdown
                       41,  ## avg Age
                       6,  ## variation in age
                       .64,  ## prob voting
                       .1,  ## variation in voting
                       candidates,  ## candidates
                       [.1, .4, .3, .2, .4],  ## candidate pref
                       [.03, .1, .1, .05, .1],  ## variation in candidate pref
                       .35,  # spectrum
                       .05,  # variation in spectrum
                       .1,  # immigrant prob
                       [.05, .4, .4, .2, .2])  ## immigrant pref)
    regions = [r1, r2, r3, r4]

    for region in regions:
        pickle.dump(region, open(region.name + ".rgn", "wb"))


if __name__ == '__main__':
    main()