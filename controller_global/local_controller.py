#!/usr/bin/python
import os
import subprocess


logfile=open('./Thakaria_hw4_track2_log1.log','r')

data=logfile.read().split('\n')

ncpu = data[-4].split()[4]
memory= 10240
core= 10

average=0.00
try:
	for i in range(-4,-35,-3):
		average=average+float(data[i].split()[4])
	average = average/10; 
except IndexError:
	average = data[-4].split()[4]
print("Average",average)

if average <=60.0:
	os.system("yarn rmadmin -updateNodeResource ms0905.utah.cloudlab.us:42205 "+str(memory+1024)+" "+str(core+1))
else:
	os.system("yarn rmadmin -updateNodeResource ms0905.utah.cloudlab.us:42205 "+str(memory-1024)+" "+str(core-1))


