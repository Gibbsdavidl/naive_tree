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
        if len(target) > 1:
            s = set(self.gene_network.gr.subcomponent(source, mode="out"))  # nodes reachable from source
            t = set([])
            for ti in target:
                t = set(t.union( set(self.gene_network.gr.subcomponent(ti, mode="in")) ) ) # nodes that can reach target
        else:
            s = set(self.gene_network.gr.subcomponent(source, mode="out")) # nodes reachable from source
            t = set(self.gene_network.gr.subcomponent(target, mode="in"))  # nodes that can reach target
        return(s.intersection(t))

    def prune_tree(self, vs):
        # subset gene_network by vs
        self.pruned_graph = self.gene_network.gr.subgraph(vs)
        return(self.pruned_graph)

    def get_spanning_tree(self):
        # subset gene_network by vs
        return(self.pruned_graph.spanning_tree(return_tree=True))

    def compute_conditionals(self, pruned=True):
        #
        flag = 10
        for ei in self.pruned_graph.es:
            if pruned == True:
                if flag < 0:
                    break;
                else:
                    print('edge id ' + str(ei.index))
                    print('from ' + ei.source_vertex['name'])
                    print('to   ' + ei.target_vertex['name'])
                    print('from idx ' + str(ei.source))
                    print('to idx ' + str(ei.target))

        return(True)