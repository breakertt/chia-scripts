import os
from datetime import datetime
import time
import math
import multiprocessing
import shutil
import random

def get_hdd_list_available(hdd_list):
  hdd_list_available = []
  for i in range(len(hdd_list)):
    total, used, free = shutil.disk_usage("/mnt/" + hdd_list[i])
    if free > 103*1024*1024*1024*1:
      hdd_list_available.append("/mnt/" + hdd_list[i])
  return hdd_list_available
  
with open("ssd_list.txt") as f:
   ssd_list = f.read().splitlines()
ssd_list = [x for x in ssd_list if x]

with open("hdd_list.txt") as f:
   hdd_list = f.read().splitlines()
hdd_list = [x for x in hdd_list if x]

with open("parallel_per_ssd.txt") as f:
   parallel_per_ssd = int(f.read())

plots = []

for ssd in ssd_list:
  for root, dirs, files in os.walk("/mnt/"+ssd, topdown=False):
    for name in files:
      if name.find('2.tmp') != -1:
        plots.append((os.path.join(root, name),name))
       
idx = 0
while True:
  hdd_list_available = get_hdd_list_available(hdd_list)
  if len(hdd_list_available) < 1:
    break
  if idx >= len(plots)-1:
    break
  root_new = hdd_list_available[0] + '/'
  name_new = plots[idx][1].replace('plot.2.tmp','plot')
  print("Move {} to {}".format(plots[idx][0], root_new + plots[idx][1]))
  shutil.move(plots[idx][0], root_new + plots[idx][1])
  print("Rename {} to {}".format(root_new + plots[idx][1], root_new + name_new))
  os.rename(root_new + plots[idx][1], root_new + name_new)
  idx += 1
