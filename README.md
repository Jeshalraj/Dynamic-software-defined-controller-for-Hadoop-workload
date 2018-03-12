### This is readme guide to get the monitor working###

##Components in the folder##

monitor.sh- This is the main monitor script which has to be run on the terminal to record the node and task data. It keeps running and collecting stats every 2 seconds and CTRL+C or CTRL+\ can be used to stop it.
controller.py - This is the basic controller implemented in python, which for now just records the outputs of NODE and TASK info in corresponding log files (LMaster.log for master, log1.log for slave1, log2.log for slave2).
sar_all.awk, sar_ps_all.awk,jps_all.awk - These are all awk scripts to filter the output of sar,ps and jps commands and generate outputs in required format. These files have to be in same folder or location as the monitor.sh.                                                                   The monitor uses this files for its operations. 
local_controller.py - parses log files and creates a flag file to transfer flags to global unit and make changes to resources locally
global_controller.py - parses log files and flag file from local and depending on the flag, increases or decreases the AMRP

##Running Monitor on nodes##

1) Copy the controller_global folder to the master node to be measured
2) Copy the controller_local folder to the slave node to be measured
3) Run a workload on master, then start monitor.sh on the slave nodes followed by local_controller.py on slave nodes and finally global_controller.py on master 

#Things to change in script before running:

1)In slave node controller, the files are provided to be run for slave 1 and hence a few changes need to be made to run the same file on slave 2

Changes in local_controller script:
 for the script in slave 2 :

logfile= open('./Thakaria_hw4_track2_log2.log','r')
flag=open('./flag_2.txt','w')

In local_controller.py for both slaves:

for command yarn rmadmin -updateNodeResources  nodeaddress: NODEID(this has to be changed according to the machine) memory vcores

