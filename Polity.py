__author__ = 'mbardoe'


class Polity(object):
    def __init__(self):
        self.regions = []


    def addRegion(self, reg):
        self.regions.append(reg)

    def population(self):
        result = 0
        for region in self.regions:
            result += region.populationSize()
        return result


