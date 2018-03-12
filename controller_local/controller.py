#!/usr/bin/python

def write_to_file():
 f1 = open("test.txt","r")
 first_line_hostname= f1.readline().split()[2]
 if(first_line_hostname.find('master')!= -1):
	filename="Thakaria_hw4_track2_LMonitor.log"
 elif(first_line_hostname.find('slave1')!= -1):
	filename="Thakaria_hw4_track2_log1.log"
 elif(first_line_hostname.find('slave2')!= -1):
	filename="Thakaria_hw4_track2_log2.log"
 else:
	print("Error in the test file")  
 f1.seek(0)
 f2 =open(filename,"a")
 for line in f1:
	f2.write(line)
 f2.write("\n")
 f2.close()
 f1.close()

if __name__ == '__main__':
 write_to_file()	
