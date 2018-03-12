#!/usr/bin/python
import os
import subprocess

memory= 10240
core= 10

while True:
	logfile=open('./Thakaria_hw4_track2_log1.log','r')
	flag=open('./flag_1.txt','w')
	data=logfile.read().split('\n')
	average=0.00
	maxcnt=0
	inc=False
	average = data[-4].split()[4]
	if (float(average) <= 60.0 and memory < 32768):
		os.system("yarn rmadmin -updateNodeResource ms0905.utah.cloudlab.us:42205 "+str(memory+1024)+" "+str(core+1))
		memory=memory+1024
		maxcnt = (memory)/1024
		inc = True

	elif(memory > 0 and memory!=32768):
		os.system("yarn rmadmin -updateNodeResource ms0905.utah.cloudlab.us:42205 "+str(memory-1024)+" "+str(core-1))
		memory=memory-1024
		maxcnt = (memory)/1024
	
	else:
		os.system("yarn rmadmin -updateNodeResource ms0905.utah.cloudlab.us:42205 "+str(memory)+" "+str(core))
		memory=memory
		maxcnt = (memory)/1024
	flag.write(str(maxcnt)+" ")
	flag.write(str(inc))
	flag.close()
	os.system('sleep 3')
