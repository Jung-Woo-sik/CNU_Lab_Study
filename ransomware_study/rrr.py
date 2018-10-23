from blockchain import blockexplorer
import time
import matplotlib.pyplot as plt
import networkx as nx
import collections

f = open("./ware5.txt",'r');
lines = f.readlines()
index = 0
b = list()
#g = nx.MultiGraph()
g = nx.MultiGraph()
g2 = nx.MultiGraph()
chord = nx.DiGraph()
#pos = nx.get_node_attributes(g,'pos')
#pos = nx.spring_layout(g)
#position = nx.spectral_layout(chord)
#pos = None
addr_in = list()
addr_out = list()
addr1 = list()
addr2 = list()
addr3 = list()
addr4 = list()
addr_z = list()
addr_all = list()
label_index = 0
for data in lines:
	a = blockexplorer.get_address(data)
	
	for i in a.transactions:
#		print (index)
#		print (time.gmtime(i.time))

		for j in i.outputs:
			try:
#				print ("input")
				#print (j.address)
				addr_all.append(j.address)
			except AttributeError as a:
				print (str(a))
chord.add_nodes_from(addr_all)
chord.add_nodes_from(lines)
	
for ch in addr_all:
	chord.add_edge(lines[0],ch)

a = blockexplorer.get_address(addr_all[0])
"""
for i in a.transactions:
	for j in i.outputs:
		try:
			addr1.append(j.address)
			print (j.address)
		except AttributeError as a:
			print (str(a))
for ch1 in addr1:
	chord.add_edge(addr_all[0],ch1)
"""
a = blockexplorer.get_address(addr_all[1])
for i in a.transactions:
	for j in i.outputs:
		try:
			addr2.append(j.address)
#			print (j.address)
		except AttributeError as a:
			print (str(a))
for ch1 in addr2:
	chord.add_edge(addr_all[1],ch1)

"""
a = blockexplorer.get_address(addr_all[3])
for i in a.transactions:
	for j in i.outputs:
		try:
			addr3.append(j.address)
			print (j.address)
		except AttributeError as a:
			print (str(a))
for ch1 in addr3:
	chord.add_edge(addr_all[3],ch1)

a = blockexplorer.get_address(addr_all[4])
for i in a.transactions:
	for j in i.outputs:
		try:
			addr4.append(j.address)
			print (j.address)
		except AttributeError as a:
			print (str(a))
for ch1 in addr4:
	chord.add_edge(addr_all[4],ch1)
"""
#for q in addr2:
a = blockexplorer.get_address(addr2[1])
for i in a.transactions:
	for j in i.outputs:
		try:
			print (j.address)
			addr_z.append(j.address)
		except AttributeError as a:
			print (str(a))
for ch2 in addr_z:
	chord.add_edge(addr2[1],ch2)
position = nx.shell_layout(chord)

nx.draw_networkx_nodes(chord,position,nodelist=addr_z,node_color='yellow')

#nx.draw_networkx_nodes(chord,position,nodelist=addr1,node_color='g')
nx.draw_networkx_nodes(chord,position,nodelist=addr2,node_color='g')
#nx.draw_networkx_nodes(chord,position,nodelist=addr3,node_color='g')
#nx.draw_networkx_nodes(chord,position,nodelist=addr4,node_color='g')

nx.draw_networkx_nodes(chord,position,nodelist=lines,node_color='r')
nx.draw_networkx_nodes(chord,position,nodelist=addr_all,node_color='b')
addr1 = list()

nx.draw_networkx_edges(chord,position)
nx.draw_networkx_labels(chord,position)
plt.show()
