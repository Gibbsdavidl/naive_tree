# Import classes from your brand new package
from naive_tree import GeneTree
from naive_tree import GeneNetwork

# Create an object of Mammals class & call a method of it
myTree = GeneTree()
myTree.build_network()
myTree.print_gene_network_summary()
myTree.gene_network.print_test_edge(4140)

# then get network between source and leaf.
vs = myTree.get_subcomponent('CXCL10', 'PTGDR2')
print('subcomponent length')
print(len(vs))

# then we can check the pruned tree, given the subcomponent
print('subgraph')
print(myTree.pruned_graph.summary())

# and we can compute a spanning tree
pruned_tree = myTree.get_spanning_tree(vs)
print('spanning tree')
print(pruned_tree.summary())
