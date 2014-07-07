import kMeans
from numpy import *
import time

# dat_set = mat(kMeans.loadDataSet('ds_hash.txt'))
dat_dropship = (kMeans.loadDataSet('DEALED_D_CUSTORMER_SHIPMENT_ITEMS_DROPSHIP.txt'))
dat_other_0 = (kMeans.loadDataSet('DEALED_D_CUSTORMER_SHIPMENT_ITEMS_OTHERS_0.txt'))

print "origin date"
print len(dat_dropship)
print len(dat_other_0)

for i in dat_dropship:
	dat_other_0.append(i)

print len(dat_other_0)

dat_other_0 = mat(dat_other_0)
# dat_dropship_0 = mat(dat_dropship)



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

print time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
biKmeans_func(dat_other_0, 10, "kmean_res_cent_file_0.txt", "kmean_res_clus_file_0.txt")

print time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))