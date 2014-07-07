import apriori

dataSet = apriori.loadDataSet()
print "dataSet"
print dataSet
C1 = apriori.createC1(dataSet)
print "C1"
print C1

D=map(set, dataSet)
print "D"
print D

L1, suppData0 = apriori.scanD(D, C1, 0.5)
print "L1"
print L1
print "suppData0"
print suppData0


L,suppData = apriori.apriori(dataSet, minSupport=0.5)
print "L"
print L
print "suppData"
print suppData

rules = apriori.generateRules(L, suppData, minConf=0.7)
print "rules"
print rules

rules = apriori.generateRules(L, suppData, minConf=0.5)
print "rules"
print rules

