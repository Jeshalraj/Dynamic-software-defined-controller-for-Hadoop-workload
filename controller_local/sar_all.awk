#!/bin/awk -f
BEGIN{
 max=0;
 ORS=" ";
}
{
 if(NR==1){Nodename=$3}
 else if(NR==4) {print $1,$2,Nodename,"NODEINFO",100-$7-$9,$7,$9}
 else if(NR==7) {print $4}
 else if(NR==10){print $3}
 else if(NR==13){print $3+$4,$4,$5}
 else if(NR==16) {print $3,$8}
 else if(NR==19) {print $11}
 else if(NR>20 && NR<25) {if($11>max){max=$11;}}
 else ; 
}
END{
 print max
 print "\n"
}
