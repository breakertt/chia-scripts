#!/bin/bash

TMP=$1
DST=$2
LOG=$3
NODE=$4
SLEEP=$5

# Delete previous temp files
cd $TMP
rm -rf *

sleep $((SLEEP*360))

# Plotting
PATH=$PATH:/usr/lib/chia-blockchain/resources/app.asar.unpacked/daemon
numactl --cpunodebind=$NODE --localalloc chia plots create -k 32 -n 99 -b 8000 -t $TMP -d $DST 2>&1 | tee $LOG
