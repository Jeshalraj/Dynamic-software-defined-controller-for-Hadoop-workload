#!/usr/bin/python
import os
import subprocess
import time
import xml.etree.ElementTree as ET


tree= ET.parse("/home/hadoop/hadoop/etc/hadoop/capacity-scheduler.xml")
tree.findall('property/value')[1].text=0.2

while True:
	os.system('scp hadoop@slave1:~/controller/Thakaria_hw4_track2_log1.log ./')
	os.system('scp hadoop@slave2:~/controller/Thakaria_hw4_track2_log2.log ./')
	os.system('scp hadoop@slave1:~/controller/flag_1.txt ./')	
	os.system('scp hadoop@slave2:~/controller/flag_2.txt ./')	

	logfile1=open('./Thakaria_hw4_track2_log1.log','r')
	logfile2=open('./Thakaria_hw4_track2_log2.log','r')

	flag1=open('./flag_1.txt','r')
	flag2=open('./flag_2.txt','r')

	data1=logfile1.read().split('\n')
	data2=logfile2.read().split('\n')

	average=0.00

	curcnt_1= data1[-3].split()[6]
	curcnt_2= data2[-3].split()[6]
	while not flag1.read(1):
		os.system('scp hadoop@slave1:~/controller/flag_1.txt ./')	
		os.system('scp hadoop@slave2:~/controller/flag_2.txt ./')	
	flag1.close()
	flag1=open('./flag_1.txt','r')
	maxcnt_1= flag1.read().split()[0]
	while not flag2.read(1):
		os.system('scp hadoop@slave2:~/controller/flag_2.txt ./')	
	flag2.close()
	flag2=open('./flag_2.txt','r')
	maxcnt_2= flag2.read().split()[0]
	if(curcnt_1<maxcnt_1 or curcnt_2<maxcnt_2):
		try:
		        for i in range(-4,-35,-3):
			   average=average+float(data1[i].split()[4])+float(data2[i].split()[4])
		           average = average/10 
		except IndexError:
			average =(float(data1[-4].split()[4])+float(data2[-4].split()[4]))/2

		amrp=float((tree.findall('property/value')[1]).text)
		if(average <=60.0 and amrp<0.7):
			(tree.findall('property/value')[1]).text = str(amrp+0.1)
		else:
			tree.findall('property/value')[1].text = str(amrp-0.1)
	tree.write('/home/hadoop/hadoop/etc/hadoop/capacity-scheduler.xml')
	os.system('yarn rmadmin -refreshQueues')
	os.system('yarn node -list')
	os.system('sleep 10')


