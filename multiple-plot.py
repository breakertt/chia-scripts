import os
from datetime import datetime
import time
import math

major_sleep_seconds = 1800
minor_sleep_seconds = 300

def getCommand(ssd, hdd, i):
    script = "/home/breakertt/chia-scripts/plot.sh"
    tmp = "/mnt/" + ssd
    dst = "/mnt/" + hdd
    log = "/home/breakertt/log/" + ssd + "-" + str(i) + "-" + datetime.now().isoformat(timespec='microseconds') + ".log"
    if ssd_list.index(ssd) < len(ssd_list) // 2:
        node = "0"
    else:
        node = "1"
    command = script + " " + tmp + " " + dst + " " + log + " " + node + " " + str(i*major_sleep_seconds + ssd_list.index(ssd)*minor_sleep_seconds)
    print(command)
    return command

with open("ssd_list.txt") as f:
   ssd_list = f.read().splitlines()
ssd_list.remove('')

with open("hdd_list.txt") as f:
   hdd_list = f.read().splitlines()
ssd_list.remove('')

parallel_per_ssd = 8
hdd_patition_len = math.ceil((len(ssd_list) * parallel_per_ssd) / len(hdd_list))
for ssd in ssd_list:
    os.system("tmux kill-session -t " + ssd)
    os.system("tmux new -d -s " + ssd)
    for i in range(parallel_per_ssd):
        hdd = hdd_list[(ssd_list.index(ssd) * parallel_per_ssd + i) // hdd_patition_len]
        #getCommand(ssd, hdd, i)
        os.system("tmux new-window -t " + ssd + ":" + str(i+1) + " " + getCommand(ssd, hdd, i))
