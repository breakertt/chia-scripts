import os
from datetime import datetime
import time

ssd_list = ["nvme0n1", "nvme1n1", "nvme2n1", "nvme3n1"]

def getCommand(ssd, i):
    script = "/home/breakertt/toys/plot.sh"
    plot_bin = "/home/breakertt/chia-plotter/chia-plotter-linux-amd64"
    tmp = "/mnt/" + ssd
    dst = "/mnt/sda"
    log = "/home/breakertt/log/" + ssd + "-" + str(i) + "-" + datetime.now().isoformat(timespec='microseconds') + ".log"
    node = str(ssd_list.index(ssd) // (len(ssd_list) // 2))
    return script + " " + plot_bin + " " + tmp + " " + dst + " " + log + " " + node

for ssd in ssd_list:
    os.system("tmux kill-session -t " + ssd)
    os.system("tmux new -d -s " + ssd)
    time.sleep(0.5)
    for i in range(1,6):
        os.system("tmux new-window -t " + ssd + ":" + str(i) + " " + getCommand(ssd, i))
