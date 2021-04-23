import os
from datetime import datetime
import time

ssd_list = ["nvme0n1", "nvme1n1", "nvme2n1", "nvme3n1"]

def getCommand(ssd, i):
    script = "/home/breakertt/toys/plot.sh"
    tmp = "/mnt/" + ssd
    dst = "/mnt/sda/official"
    log = "/home/breakertt/log/" + ssd + "-" + str(i) + "-" + datetime.now().isoformat(timespec='microseconds') + ".log"
    if ssd_list.index(ssd) < len(ssd_list) // 2:
        node = "0"
    else:
        node = "1"
    return script + " " + " " + tmp + " " + dst + " " + log + " " + node + " " + str(i-1)

for ssd in ssd_list:
    os.system("tmux kill-session -t " + ssd)
    os.system("tmux new -d -s " + ssd)
    time.sleep(0.5)
    for i in range(1,8):
        os.system("tmux new-window -t " + ssd + ":" + str(i) + " " + getCommand(ssd, i))
