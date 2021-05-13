#!/bin/bash

while true
do
        echo $(date -Iseconds)
        echo $(du -sh /home/breakertt/chia/tmp/)
        echo $(sudo smartctl -a /dev/nvme0n1 | grep "Data Unit")
        sleep 60
done
