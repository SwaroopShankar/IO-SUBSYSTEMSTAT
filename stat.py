#importing necessary packages

import time
import os
import sys
import re


#To display the device layer statistics
def deviceStat():
	print("IOSTAT with 2 sec interval::")
	print("---------------------------")
	print("---------------------------")
	
#printing the iostat at 2 sec interval 3 times
	for i in range(3):
		
		iostat = os.popen("iostat sda ").read()
		print(iostat)
		time.sleep(1)

	print("sda/stat::")
	print("---------------------------")
	print("---------------------------")

#User inputs the time gap for the sda/stat files
	timer = int(input("Enter the time interval between sda/stats:"))

#The sda/stat at present time is read and preprocessed using regular expressions.
	stats = os.popen("cat /sys/block/sda/stat").read()
	stats_split = re.sub(r"\s+", " ", stats, flags=re.UNICODE)
	stats_split = stats_split.strip()
	stats_split = stats_split.split(' ')
	stats_array = stats_split
#The stat is stored in the form of a list
	time.sleep(timer)
	stats_2 = os.popen("cat /sys/block/sda/stat").read()
	stats_split_2 = re.sub(r"\s+", " ", stats_2, flags=re.UNICODE)
	stats_split_2 = stats_split_2.strip()
	stats_split_2 = stats_split_2.split(' ')
	stats_array_2 = stats_split_2

	iototal = [
	int(stats_array_2[0]) - int(stats_array[0]),
	int(stats_array_2[1]) - int(stats_array[1]),
	int(stats_array_2[2]) - int(stats_array[2]),
	int(stats_array_2[3]) - int(stats_array[3]),
	int(stats_array_2[4]) - int(stats_array[4]),
	int(stats_array_2[5]) - int(stats_array[5]),
	int(stats_array_2[6]) - int(stats_array[6]),
	int(stats_array_2[7]) - int(stats_array[7]),
	int(stats_array_2[8]) - int(stats_array[8]),
	int(stats_array_2[9]) - int(stats_array[9]),
	int(stats_array_2[10]) - int(stats_array[10])
	]
	 
	description = [
	"IO stats over last "+str(timer)+" seconds \n\n",
	"read I/Os : {}".format(iototal[0]),
	"read merges : {}".format(iototal[1]),
	"read sectors : {}".format(iototal[2]),
	"read ticks (ms) : {}".format(iototal[3]),
	"write I/Os : {}".format(iototal[4]),
	"write merges : {}".format(iototal[5]),
	"write sectors : {}".format(iototal[6]),
	"write ticks (ms) : {}".format(iototal[7]),
	"in_flight : {}".format(iototal[8]),
	"io_ticks (ms) : {}".format(iototal[9]),
	"time_in_queue (ms) : {}".format(iototal[10])
	]
	for d in description:
		print(d)

def partitionStat():

    print("sda stats of each partitions::")
    print("---------------------------")
    print("---------------------------")
    print()
    print("sda1 stat:")	
    stats1 = os.popen("cat /sys/block/sda/sda1/stat").read()
    print(stats1)
    print()
    print("sda2 stat:")	
    stats2 = os.popen("cat /sys/block/sda/sda2/stat").read()
    print(stats2)
    print()
    print("sda3 stat:")	
    stats3 = os.popen("cat /sys/block/sda/sda3/stat").read()
    print(stats3)
    print()
    print("sda4 stat:")
    stats4 = os.popen("cat /sys/block/sda/sda4/stat").read()
    print(stats4)
    print()
    print("sda5 stat:")	
    stats5 = os.popen("cat /sys/block/sda/sda5/stat").read()
    print(stats5)
    print()	
    statsPartitions= [stats1,stats2,stats3,stats4,stats5]
    for i,stats in enumerate(statsPartitions):


        stats_array = re.sub(r"\s+", " ", stats, flags=re.UNICODE)
        stats_split = stats_array.strip()
        stats_array = stats_split.split(' ')
        description = [
		"read I/Os : {}".format(stats_array[0]),
		"read merges : {}".format(stats_array[1]),
		"read sectors : {}".format(stats_array[2]),
		"read ticks (ms) : {}".format(stats_array[3]),
		"write I/Os : {}".format(stats_array[4]),
		"write merges : {}".format(stats_array[5]),
		"write sectors : {}".format(stats_array[6]),
		"write ticks (ms) : {}".format(stats_array[7]),
		"in_flight : {}".format(stats_array[8]),
		"io_ticks (ms) : {}".format(stats_array[9]),
		"time_in_queue (ms) : {}".format(stats_array[10])
		]
        file_object = open('sda{}.txt'.format(i+1), 'w') 
        for d in description:
            file_object.write(str(d))
            file_object.write("\n")


	




#To display the disk layer statistics
def blockStat():
	print("Blockstat - Parsing the blocktrace files with blkparse::")
	print("--------------------------------------------------------")
	core = int(input("Enter the sda core which you want to trace:"))
	# os.popen("sudo blktrace /dev/sda -w 2")
	os.popen("sudo blkparse -i /home/swaroop/SubSystemStat/sda.blktrace.{} > /home/swaroop/SubSystemStat/blkparse.txt".format(core))
	# btt command for analysing the latency
	os.system("sudo btt -i sda.blktrace.3 > /home/swaroop/SubSystemStat/btt.txt")
	print("Parsing done and dumped into blktrace.txt and btt.txt respectively")
	print()

#To trace the function calls and analyse the latencies
def ftrace_function():
	
	os.chdir(r"/sys/kernel/debug/tracing")
	os.popen("sudo echo 1 > tracing_max_latency")
	os.popen("sudo echo ext4* > set_ftrace_filter")
	os.popen("echo function > current_tracer")
	os.popen("sudo echo 1 > tracing_on")
	time.sleep(3)
	os.popen("sudo echo 0 > tracing_on") 
	os.popen("cp trace /home/swaroop/SubSystemStat/trace1.txt")

def ftrace_functionGraph():
	os.chdir(r"/sys/kernel/debug/tracing")
	os.popen("sudo echo 1 > tracing_max_latency")
	os.popen("sudo echo ext4* > set_ftrace_filter")
	os.popen("echo function_graph > current_tracer")
	os.popen("sudo echo 1 > tracing_on")
	time.sleep(5)
	os.popen("sudo echo 0 > tracing_on") 
	os.popen("cp trace /home/swaroop/SubSystemStat/ftrace_functionGraph.txt")
	os.popen("cat /home/swaroop/SubSystemStat/ftrace_functionGraph.txt | grep ! -B 10 > /home/swaroop/SubSystemStat/ftrace_latency.txt")

#To trace the system calls with a specific pid passed as an argument to the program	
def strace():
	
	pid = sys.argv[1]
	os.popen("sudo echo timeout 5 strace -p {}".format(pid))
        


if __name__=="__main__":
	deviceStat()
	blockStat()
	partitionStat()
	#ftrace_function()
	ftrace_functionGraph()
	#strace()
		
