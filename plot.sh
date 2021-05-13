#!/bin/bash

TMP=$1
DST=$2
LOG=$3
NODE=$4
SLEEP=$5

# Delete previous temp files
cd $TMP
rm -rf *
cd /home/breakertt/chia-scripts/

sleep $((SLEEP))

# Plotting
PATH=$PATH:/usr/lib/chia-blockchain/resources/app.asar.unpacked/daemon

while true; do 
  DST=$(python3 get-hdd.py)
  chia plots create -k 32 -n 1 -b 8000 -t $TMP -d $DST 2>&1 | tee $LOG
done
