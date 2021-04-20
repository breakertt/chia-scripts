#!/bin/bash

BIN=$1
TMP=$2
DST=$3
LOG=$4
NODE=$5

# Delete previous temp files
cd $TMP
rm -rf *

# Plotting
cd $(dirname $BIN)
numactl --cpunodebind=$NODE --localalloc $BIN -action plotting -plotting-fpk 0xa85b3f8b4322bde2699ea4e8a5fc7c631356aeab5931e9497a20303ae616b4a95a60b091b13753d7aa79a943b478a022 -plotting-ppk 0x87eea6f6fe9d2b7d43a61e6f7f081f752112fd002a1f6986c10c3cf897d5d23be0cfeae7c7dbd712f8ad8136affbe8da -plotting-n 90 -t $TMP -d $DST 2>&1 | tee $LOG
