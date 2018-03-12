#!/bin/awk -f

BEGIN{
 am=0
 yc=0
 OFS=" "
}

{
 if($2=="MRAppMaster"){am=am+1;}
 else if($2=="YarnChild"){yc=yc+1;}
 else {am=am;yc=yc;}
}

END{
 print ((am*2)+(yc)),am,yc
}
