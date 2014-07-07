import kMeans
from numpy import *

# dat_set = mat(kMeans.loadDataSet('ds_hash.txt'))
dat_dropship = (kMeans.loadDataSet('DEALED_D_CUSTORMER_SHIPMENT_ITEMS_DROPSHIP.txt'))
dat_other_0 = (kMeans.loadDataSet('DEALED_D_CUSTORMER_SHIPMENT_ITEMS_OTHERS_0.txt'))
dat_other_1 = (kMeans.loadDataSet('DEALED_D_CUSTORMER_SHIPMENT_ITEMS_OTHERS_1.txt'))
dat_other_2 = (kMeans.loadDataSet('DEALED_D_CUSTORMER_SHIPMENT_ITEMS_OTHERS_2.txt'))
dat_other_3 = (kMeans.loadDataSet('DEALED_D_CUSTORMER_SHIPMENT_ITEMS_OTHERS_3.txt'))
dat_other_4 = (kMeans.loadDataSet('DEALED_D_CUSTORMER_SHIPMENT_ITEMS_OTHERS_4.txt'))
dat_other_5 = (kMeans.loadDataSet('DEALED_D_CUSTORMER_SHIPMENT_ITEMS_OTHERS_5.txt'))
dat_other_6 = (kMeans.loadDataSet('DEALED_D_CUSTORMER_SHIPMENT_ITEMS_OTHERS_6.txt'))

print "origin date"
print len(dat_dropship)
print len(dat_other_0)

for i in dat_dropship:
	dat_other_0.append(i)
	dat_other_1.append(i)
	dat_other_2.append(i)
	dat_other_3.append(i)
	dat_other_4.append(i)
	dat_other_5.append(i)
	dat_other_6.append(i)

print len(dat_other_0)
print len(dat_other_1)
print len(dat_other_2)
print len(dat_other_3)
print len(dat_other_4)
print len(dat_other_5)
print len(dat_other_6)

dat_other_0 = mat(dat_other_0)
dat_other_1 = mat(dat_other_1)
dat_other_2 = mat(dat_other_2)
dat_other_3 = mat(dat_other_3)
dat_other_4 = mat(dat_other_4)
dat_other_5 = mat(dat_other_5)
dat_other_6 = mat(dat_other_6)



def biKmeans_func(data_set, k, cent_file="", clus_file=""):
	print "kMeans : " + cent_file
	cent, clus = kMeans.biKmeans(data_set, k)
	# print cent
	# print clus

	kmean_res_cent_file = open(cent_file, 'w')
	for item in cent.A:
		item_str = ""
		for column in item:
			item_str = item_str + str(column) + " "
		item_str = item_str + '\n'
		kmean_res_cent_file.write(item_str)
	kmean_res_cent_file.close

	kmean_res_clus_file = open(clus_file, 'w')
	for item in clus.A:
		item_str = ""
		for column in item:
			item_str = item_str + str(column) + " "
		item_str = item_str + '\n'
		kmean_res_clus_file.write(item_str)
	kmean_res_clus_file.close

# biKmeans_func(dat_set, 2, "kmean_res_cent_file", "kmean_res_clus_file")

biKmeans_func(dat_other_0, 20, "kmean_res_cent_file_0.txt", "kmean_res_clus_file_0.txt")
biKmeans_func(dat_other_1, 20, "kmean_res_cent_file_1.txt", "kmean_res_clus_file_1.txt")
biKmeans_func(dat_other_2, 20, "kmean_res_cent_file_2.txt", "kmean_res_clus_file_2.txt")
biKmeans_func(dat_other_3, 20, "kmean_res_cent_file_3.txt", "kmean_res_clus_file_3.txt")
biKmeans_func(dat_other_4, 20, "kmean_res_cent_file_4.txt", "kmean_res_clus_file_4.txt")
biKmeans_func(dat_other_5, 20, "kmean_res_cent_file_5.txt", "kmean_res_clus_file_5.txt")
biKmeans_func(dat_other_6, 20, "kmean_res_cent_file_6.txt", "kmean_res_clus_file_6.txt")





# import matplotlib
# import matplotlib.pyplot as plt

# markers = ['rs', 'go', 'b^', 'y8', 'cp', 'm<', 'k>', 'w,',\
# 		 'ro', 'g^', 'b8', 'yp', 'c<', 'm>', 'k,', 'ws',\
# 		 'r^', 'g8', 'bp', 'y<', 'c>', 'm,', 'ks', 'wo', ]

# print 'dat_set'
# # print dat_set

# x = [dat_set[i,0] for i in range(len(dat_set))]
# # print x
# y = [dat_set[i,1] for i in range(len(dat_set))]
# # print y

# print markers[int(clus[i, 0])]

# for i in range(len(dat_set)):
# 	plt.plot(x[i], y[i], markers[int(clus[i, 0])])
# plt.show()
