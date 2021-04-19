#!/bin/bash

tmux kill-session -t miner
tmux new -d -s miner
tmux send-keys -t miner:0 "cd /home/breakertt/chia-miner/; /home/breakertt/chia-miner/hpool-miner-chia" ENTER
