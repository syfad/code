#!/bin/bash

fdisk /dev/xvdb <<EOF
n
p
1


w

EOF
mkfs.ext4 /dev/xvdb1
mkdir -p /dmdata
UUID=`/sbin/blkid /dev/xvdb1 | awk -F"\"" '{print $2}'`
mount -U $UUID  /dmdata
#mount /dev/xvdb1 /dmdata
UUID_DIR="UUID="$UUID
echo "${UUID_DIR}        /dmdata                 ext4    defaults    0  0">>/etc/fstab
mkdir -p /dmdata/{apps,install,data,logs,scripts,server,www,backups,tmp}
chown -R deve.deve /dmdata
