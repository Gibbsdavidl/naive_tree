import pandas as pd

class GeneNetwork:
    def __init__(self):
        ''' Constructor for this class. '''
        self.size = 0 # number of genes in the tree
        self.f1 = []
        self.f2 = []
        self.f3 = []

    def printTableSizes(self):
        print('table f1 ' + str(len(self.f1)) + ' rows in it.')
        print('table f2 ' + str(len(self.f2)) + ' rows in it.')
        print('table f3 ' + str(len(self.f3)) + ' rows in it.')

    def readNetworkFiles(self):
        self.f1 = pd.read_csv('naive_tree/data/lr_network.csv.gz')
        self.f2 = pd.read_csv('naive_tree/data/gr_network.csv.gz')
        self.f3 = pd.read_csv('naive_tree/data/sig_network.csv.gz')
