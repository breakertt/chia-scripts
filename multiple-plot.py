import os
from datetime import datetime
import time
import math
import multiprocessing

def getCommand(ssd, hdd, i):
    script = "/home/breakertt/chia-scripts/plot.sh"
    tmp = "/mnt/" + ssd
    dst = "/mnt/" + hdd
    log = "/home/breakertt/log/" + ssd + "-" + str(i) + "-" + datetime.now().isoformat(timespec='microseconds') + ".log"
    if ssd_list.index(ssd) < len(ssd_list) // 2:
        node = "0"
    else:
        node = "1"
    command = script + " " + tmp + " " + dst + " " + log + " " + node + " " + str((ssd_list.index(ssd) + i*len(ssd_list)) * sleep_seconds)
    print(command)
    return command

with open("ssd_list.txt") as f:
   ssd_list = f.read().splitlines()
ssd_list = [x for x in ssd_list if x]

with open("hdd_list.txt") as f:
   hdd_list = f.read().splitlines()
hdd_list = [x for x in hdd_list if x]

with open("parallel_per_ssd.txt") as f:
   parallel_per_ssd = int(f.read())

plot_hours = 13
sleep_seconds = (plot_hours * 3600) // (parallel_per_ssd * len(ssd_list))

hdd_patition_len = math.ceil((len(ssd_list) * parallel_per_ssd) / len(hdd_list))
for ssd in ssd_list:
    os.system("tmux kill-session -t " + ssd)
    os.system("tmux new -d -s " + ssd)
    for i in range(parallel_per_ssd):
        hdd = hdd_list[(ssd_list.index(ssd) * parallel_per_ssd + i) // hdd_patition_len]
        #getCommand(ssd, hdd, i)
        os.system("tmux new-window -t " + ssd + ":" + str(i+1) + " " + getCommand(ssd, hdd, i))
