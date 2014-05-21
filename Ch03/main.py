import trees
import treePlotter
treePlotter.retrieveTree(1)
myTree = treePlotter.retrieveTree(0)

fr = open('lenses.txt')
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels=['age', 'prescript', 'astigmatix', 'tearRate']
lensesTree = trees.createTree(lenses, lensesLabels)
treePlotter.createPlot(lensesTree)

