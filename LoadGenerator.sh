#!/bin/bash
#install Load Generator

Name=Linux
SoftPath=/dmdata/install/
yum -y install  libgcc_s.so.1 libm.so.6  libstdc++.so.5 c++
cd /dmdata/install
wget http://172.16.0.121:8080/dir/$Name.zip
unzip $Name.zip
chmod +x $Name -R
cd $Name
useradd -g 0 -s /bin/bash hp_load
cat << EOF >> /etc/profile
export PRODUCT_DIR=/opt/HP/HP_LoadGenerator
export M_LROOT=\$PRODUCT_DIR
export LD_LIBRARY_PATH=\${M_LROOT}/bin 
export PATH=\${M_LROOT}/bin:\$PATH
EOF
source /etc/profile
$SoftPath$Name/installer.sh <<EOF
n
a
i
f
EOF
su - hp_load
cd /opt/HP/HP_LoadGenerator/bin
sh verify_generator
./m_daemon_setup start
