import shutil
import random

with open("hdd_list.txt") as f:
  hdd_list = f.read().splitlines()

hdd_list_available = []
for i in range(len(hdd_list)):
  total, used, free = shutil.disk_usage("/mnt/" + hdd_list[i])
  if free > 101*1024*1024*1024*4:
    hdd_list_available.append("/mnt/" + hdd_list[i])
    
hdd_selected = random.choice(hdd_list_available)

print(hdd_selected)
