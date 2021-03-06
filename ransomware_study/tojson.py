from blockchain import blockexplorer
import time
import matplotlib.pyplot as plt
import networkx as nx
import collections
import csv
import json

f = open("./ware6.txt",'r');
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
json_list = list()
addr_in = list()
addr_out = list()
addr_top = list()
addr1 = list()
addr2 = list()
addr3 = list()
addr4 = list()
addr_z = list()
addr_all = list()
str_json =''
label_index = 0
with open('./out.json','w') as jsonfile:
#	fieldname =['address','out_addr']
#	writer = csv.DictWriter(csvfile,fieldnames=fieldname)
#	writer.writeheader()
	for data in lines:
		a = blockexplorer.get_address(data)
		addr_top.append(a.address)
	#	str_json = str_json + "{\"name\" : \"" +a.address+ "\",\"children\" : [ "
		for i in a.transactions:
#			print (index)
#			print (time.gmtime(i.time))
			outaddr = ""
			inaddr =""
			for j in i.outputs:
				try:
#					print ("input")
					#print (j.address)
					addr_all.append(j.address)
					outaddr = outaddr + j.address +" "
		#			str_json = str_json + "{\"name\" : \""+j.address+"\"}"
				except AttributeError as a:
					print (str(a))	
#			writer.writerow({'address':a.address ,'out_addr':outaddr})
			break
#		addr_all.remove(a.address)
	for data in addr_all:
		a = blockexplorer.get_address(data)
		for i in a.transactions:
			outaddr = ""
			for j in i.outputs:
				try:
					outaddr = outaddr + j.address +" "
					addr1.append(j.address)
				except AttributeError as a:
					print (str(a))
#			writer.writerow({'address':a.address,'out_addr':outaddr})
			break;
	for data in addr1:
		a = blockexplorer.get_address(data)
		for i in a.transactions:
			outaddr = ""
			for j in i.outputs:
				try:
					outaddr = outaddr + j.address + " "
					addr2.append(j.address)
				except AttributeError as a:
					print (str(a))
#			writer.writerow({'address':a.address,'out_addr':outaddr})
	for data in lines:
		a = blockexplorer.get_address(data);
		for i in a.transactions:
			#json_list.append({"name" :  a.address }, )
			str_json = str_json + "{\'name\' : \'"+a.address +"\'},\'children\':"
			for j in i.outputs:
				try:
					#json_list.append(["children" : {"name" : j.address,}])
					str_json = str_json +"{\'name' : \'"+j.address+"\'},"
					print(j.address)
				except AttributeError as a:
					print (str(a))
			str_json = str_json+"]}"
			break
	#			str_json = str_json + "]"
	#json_acceptable_string = str_json.replace("'","\'")
#	d = json.loads(str_json)
	json.dump(str_json,jsonfile)
