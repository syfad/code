#!/bin/bash

CPU1=`cat /proc/stat | grep "$1" | awk '{print $2" "$3" "$4" "$5" "$6" "$7" "$8}'`
sleep 5
CPU2=`cat /proc/stat | grep "$1" | awk '{print $2" "$3" "$4" "$5" "$6" "$7" "$8}'`

IDLE1=`echo $CPU1 | awk '{print $4}'`
IDLE2=`echo $CPU2 | awk '{print $4}'`

CPU1_TOTAL=`echo $CPU1 | awk '{print $1+$2+$3+$4+$5+$6+$7}'`
CPU2_TOTAL=`echo $CPU2 | awk '{print $1+$2+$3+$4+$5+$6+$7}'`

#IDLE=`echo "$IDLE2-$IDLE1" | bc`
IDLE=`expr $IDLE2 - $IDLE1`
CPU_TOTAL=`expr $CPU2_TOTAL - $CPU1_TOTAL`

RATE=`echo "scale=4;($CPU_TOTAL-$IDLE)/$CPU_TOTAL*100" | bc | awk '{printf "%.2f",$1}'`

#echo $IDLE
#echo $CPU_TOTAL
echo $RATE
