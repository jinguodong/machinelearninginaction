from numpy import *

a = range(10)
print a
for i in range(10):
	rand_i = int(random.uniform(0, len(a)))
	del(a[rand_i])
	print rand_i
	print a

print rand_i