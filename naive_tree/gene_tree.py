from gene_network import GeneNetwork

class GeneTree:
    def __init__(self):
        ''' Constructor for this class. '''
        self.gene_network = None
        self.pruned_graph = None

    def print_gene_network_summary(self):
        self.gene_network.print_summary()

    def build_network(self):
        gnet = GeneNetwork()
        gnet.make_graph()
        self.gene_network = gnet

    def get_subcomponent(self, source, target):
        #https://stackoverflow.com/questions/29314795/python-igraph-get-all-possible-paths-in-a-directed-graph
        s = set(self.gene_network.gr.subcomponent(source, mode="out")) # nodes reachable from source
        t = set(self.gene_network.gr.subcomponent(target, mode="in"))  # nodes that can reach target
        return(s.intersection(t))

    def get_spanning_tree(self, vs):
        # subset gene_network by vs
        self.pruned_graph = self.gene_network.gr.subgraph(vs)
        return(self.pruned_graph.spanning_tree(return_tree=True))
