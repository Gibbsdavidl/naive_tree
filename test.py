# Import classes from your brand new package
from naive_tree import GeneTree
from naive_tree import GeneNetwork

# Create an object of Mammals class & call a method of it
myTree = GeneTree()
myTree.build_network()
myTree.print_gene_network_summary()
myTree.gene_network.print_test_edge(4140)

# then get network between source and list-of-leaves.
vs = myTree.get_subcomponent(source='CXCL10', target=['PTGDR2','PTGDR'])
print('subcomponent length')
print(len(vs))

# and we can prune the tree to just nodes
# reachable from the source
myTree.prune_tree(vs)

# doing a search starting from the root to make sure we can
# reach all nodes
vs = myTree.pruned_graph.bfs(
            myTree.pruned_graph.vs.find(name='CXCL10').index,
            mode='out')

print('len vs: ' + str(len(vs[0])))

# and we can create a spanning tree based on
# edge weights.
myTree.get_spanning_tree()

myTree.compute_conditionals()