import os
from datetime import datetime
import time
import math

def getCommand(ssd, hdd, i):
    script = "/home/breakertt/toys/plot.sh"
    tmp = "/mnt/" + ssd
    dst = "/mnt/" + hdd
    log = "/home/breakertt/log/" + ssd + "-" + str(i) + "-" + datetime.now().isoformat(timespec='microseconds') + ".log"
    if ssd_list.index(ssd) < len(ssd_list) // 2:
        node = "0"
    else:
        node = "1"
    command = script + " " + tmp + " " + dst + " " + log + " " + node + " " + str(i)
    print(command)
    return command

ssd_list = ["nvme0n1", "nvme1n1", "nvme2n1", "nvme3n1"]
hdd_list = ["sda", "sdb", "sdc", "sdd", "sde", "sdf", "sdg", "sdh"]
parallel_per_ssd = 7
hdd_patition_len = math.ceil((len(ssd_list) * parallel_per_ssd) / len(hdd_list))
for ssd in ssd_list:
    os.system("tmux kill-session -t " + ssd)
    os.system("tmux new -d -s " + ssd)
    for i in range(parallel_per_ssd):
        hdd = hdd_list[(ssd_list.index(ssd) * parallel_per_ssd + i) // hdd_patition_len]
        #getCommand(ssd, hdd, i)
        os.system("tmux new-window -t " + ssd + ":" + str(i+1) + " " + getCommand(ssd, hdd, i))
