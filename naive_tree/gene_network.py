
import pandas as pd
import igraph

class GeneNetwork:
    def __init__(self):
        ''' Constructor for this class. '''
        self.size = 0 # number of genes in the tree
        self.f1 = []
        self.f2 = []
        self.f3 = []
        self.edges = []
        self.gene_to_idx = dict()
        self.idx_to_gene = dict()
        self.gr = None

    def print_summary(self):
        print('table lr_network ' + str(len(self.f1)) + ' rows in it.')
        print('table gr_network ' + str(len(self.f2)) + ' rows in it.')
        print('table sig_network ' + str(len(self.f3)) + ' rows in it.')
        print('graph summary:')
        print(self.gr.summary())

    def print_test_edge(self, idx):
        print('edge ' + str(idx))
        print(self.edges.iloc[idx])
        print('edge from graph')
        edge = self.gr.es[idx]
        print(edge.source)
        print(edge.target)
        print(self.gr.vs[edge.source])
        print(self.gr.vs[edge.target])

    def read_network_files(self):
        self.f1 = pd.read_csv('naive_tree/data/lr_network.csv.gz')
        self.f2 = pd.read_csv('naive_tree/data/gr_network.csv.gz')
        self.f3 = pd.read_csv('naive_tree/data/sig_network.csv.gz')

    def make_vertex_list(self, edges):
        nodes = set(edges['from'].tolist() + edges['to'].tolist())
        return(list(nodes))

    def make_node_dict(self, vertex_list):
        self.idx_to_gene = {idx: gene for idx,gene in enumerate(vertex_list)}
        self.gene_to_idx = {gene: idx for idx,gene in enumerate(vertex_list)}

    def make_edge_list(self, edges):
        edge_list = []
        for i in range(0,len(edges)):
            edge_list.append( (self.gene_to_idx[edges['from'].iloc[i]], self.gene_to_idx[edges['to'].iloc[i]]) )
        return(edge_list)

    def make_edges(self):
        f1edges = self.f1[['from', 'to']]
        f2edges = self.f2[['from', 'to']]
        f3edges = self.f3[['from', 'to']]
        edges = f1edges.append(f2edges)
        self.edges = edges.append(f3edges)

    def make_graph(self):
        # first read in the nichenet files
        self.read_network_files()
        # then format them to a 2 column table [from , to]
        self.make_edges()
        # make a vertex list that aligns with dict
        vertex_list = self.make_vertex_list(self.edges)
        # make a node dict for looking up node names
        self.make_node_dict(vertex_list)
        # convert the edges to numeric
        edge_list = self.make_edge_list(self.edges)
        # then build the graph
        self.gr = igraph.Graph(directed=True)
        self.gr.add_vertices(vertex_list)
        self.gr.add_edges(edge_list)

