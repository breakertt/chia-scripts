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
    command = script + " " + tmp + " " + dst + " " + log + " " + node + " " + str(i-1)
    print(command)
    return command

ssd_list = ["nvme0n1", "nvme1n1", "nvme2n1", "nvme3n1"]
hdd_list = ["sda", "sdb"]
for ssd in ssd_list:
    os.system("tmux kill-session -t " + ssd)
    os.system("tmux new -d -s " + ssd)
    time.sleep(0.5)
    hdd_patition_len = math.ceil(len(ssd_list) // len(hdd_list))
    hdd = hdd_list[ssd_list.index(ssd) // hdd_patition_len]
    for i in range(1,8):
        getCommand(ssd, hdd, i)
        os.system("tmux new-window -t " + ssd + ":" + str(i) + " " + getCommand(ssd, hdd, i))
