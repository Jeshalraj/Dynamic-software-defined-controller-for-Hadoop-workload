#!/bin/bash

echo "Starting the monitor....\n Press CTRL+C or CTRL+\ to end recording"
trap 'my_exit' SIGINT SIGQUIT

my_exit(){
  echo "Terminating..."
  exit 
}

while true 
do
sar -uwbrqd -n DEV 1 1 |awk -f sar_all.awk > test.txt
tail -2 test.txt
export HOSTNAME
ps -w -w -m aux| grep "org.apache.hadoop" |awk -f sar_ps_all.awk >>test.txt
jps | awk -f jps_all.awk >> test.txt
tail -1 test.txt
python controller.py
echo "Registering Entry."
sleep 2
done
