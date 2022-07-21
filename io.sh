#! /bin/bash 


file='io.txt'  
  
i=1  
while read line; do  
   
i=$((i+1))  
done < $file  


for num in {1..10000}  
do  
file='io.txt'  
  
i=1  
while read line; do  
   
i=$((i+1))  
done < $file  
dd if=/home/swaroop/SubSystemStat/io.txt of=/mnt/test1 bs=1M count=1
done  
