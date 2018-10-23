from blockchain import blockexplorer
import time
import networkx as nx

input_tx0 = '1P39C9NVmZfqeVfkBMp7ng4PvJTWwNKLjp' 	#cerber
#input_tx1 = '1Eva3QASjLY4YsxkqnfRoYj6PGWGeYNkBq'
#input_tx2 = '1Dj9YnMiciNgaKuyzKynygu7nB21tvV6QD'
#input_tx3 = '1C258J43so5QYiSHifJQ8FYDEMgJX6dHTg'
input_tx4 = '1MM1vMc8a2PrenvToofWg9FxgfQTqUnANF'	#cerber
input_tx5 = '1sZw3i8ACmMP9BSg5sfYAwBDRzPijbiuE'
input_tx6 = '18v9RXkSstrabrpDToxNEF1h65ygDDLcp3'
input_tx7 = '12JyhyxzTafnPc5vHELZRVSFqvy2RAdFNE'
input_tx8 = '145B1mxyZEC62JDMUHUGVFcu938uvzU6Xt'
a = blockexplorer.get_address(input_tx8)
b = list()
c = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
for i in a.transactions:
	print (i)
	print (time.gmtime(i.time))
	for j in i.inputs:
		try:
			print (j.address)
			print (j.value)
		except AttributeError as a:
			print (str(a))
	print ("out")
	for o in i.outputs:
		try:
			print (o.address)
			print (o.value)
		except AttributeError as a:
			print (str(a))
#b.sort()
#d = 0
#f =list()

#for i in c:
#	for j in b:
#		if i==j:
#			d=d+1
#		else:
#			continue
#	f.append(d)
#	d=0
#print (b)
#print (f)
#plt.plot(c,f)
#plt.axis([0,24,0,14])
#plt.show()

#plt.plot(c,f[9:24]+f[:9])
#plt.axis([0,24,0,14])
#plt.show()

