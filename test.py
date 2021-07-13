# Import classes from your brand new package
from naive_tree import GeneTree
from naive_tree import GeneNetwork

# Create an object of Mammals class & call a method of it
myTree = GeneTree()
myTree.printTreeSize()

myNet = GeneNetwork()
myNet.readNetworkFiles()
myNet.printTableSizes()
