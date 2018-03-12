#!/bin/awk -f
BEGIN{
 cpuper=0.0;
 memper=0.0;
 OFS=" "
 ORS=" "
}

{
 cpuper= cpuper+$3;
 memper= memper+$4;
}

END{
 print strftime("%r"),"("ENVIRON["HOSTNAME"]")","TASKINFO",cpuper,memper
}
