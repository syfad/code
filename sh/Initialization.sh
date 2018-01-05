#!/bin/sh
#系统初始化设置配置脚本

rpm -ivh http://mirrors.sohu.com/fedora-epel/6/x86_64/epel-release-6-8.noarch.rpm
rpm -Uvh http://apt.sw.be/redhat/el6/en/x86_64/rpmforge/RPMS/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm

yum clean all 
yum makecache

yum -y install ntp gcc gcc-c++ bison patch unzip mlocate flex wget automake autoconf gd cpp sysstat gettext readline-devel libjpeg-devel libpng-devel freetype-devel libxml2-devel zlib-devel glibc-devel glib2-devel bzip2-devel ncurses-devel curl-devel e2fsprogs-devel libidn-devel expat-devel libtool libtool-ltdl-devel cmake openssl-devel libevent-devel ntp gcc-c++ uuid-devel libuuid-devel libtool git openssh-clients vim


#echo '*/10 * * * * (/usr/sbin/ntpdate pool.ntp.org && hwclock -w) >/dev/null 2>&1' >>/var/spool/cron/root
#crontab -l

/usr/sbin/setenforce 0
sed -i 's#SELINUX=enforcing#SELINUX=disabled#g' /etc/sysconfig/selinux
sed -i 's#SELINUX=enforcing#SELINUX=disabled#g' /etc/selinux/config

sed -i '/# End of file/ i\*       soft    nofile          65535' /etc/security/limits.conf 
sed -i '/# End of file/ i\*       hard    nofile          65535' /etc/security/limits.conf 
sed -i 's/tty\[1-6\]/tty\[1-2\]/g' /etc/sysconfig/init 
sed -i 's/*          soft    nproc     1024/*          soft    nproc     65535/g' /etc/security/limits.d/90-nproc.conf 

useradd deve -u 544

modprobe nf_conntrack
echo "modprobe nf_conntrack">> /etc/rc.local

cp /etc/sysctl.conf{,.$(date +%F)}
cat >/etc/sysctl.conf<<EOF
net.ipv4.ip_forward = 0
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.default.accept_source_route = 0
kernel.sysrq = 0
kernel.core_uses_pid = 1
net.ipv4.tcp_syncookies = 1
net.bridge.bridge-nf-call-ip6tables = 0
net.bridge.bridge-nf-call-iptables = 0
net.bridge.bridge-nf-call-arptables = 0
kernel.msgmnb = 65536
kernel.msgmax = 65536
kernel.shmmax = 68719476736
kernel.shmall = 4294967296
net.ipv4.tcp_max_tw_buckets = 40000 
net.ipv4.tcp_sack = 1 
net.ipv4.tcp_window_scaling = 1 
net.core.wmem_default = 8388608 
net.core.rmem_default = 8388608 
net.core.rmem_max = 16777216 
net.core.wmem_max = 16777216 
net.core.netdev_max_backlog = 262144 
net.core.somaxconn = 262144 
net.core.optmem_max = 81920 
net.ipv4.tcp_max_orphans = 3276800 
net.ipv4.tcp_max_syn_backlog = 262144 
net.ipv4.tcp_timestamps = 0 
net.ipv4.tcp_synack_retries = 1 
net.ipv4.tcp_syn_retries = 1 
net.ipv4.tcp_tw_recycle = 1 
net.ipv4.tcp_tw_reuse = 1 
net.ipv4.tcp_mem = 94500000 915000000 927000000 
net.ipv4.tcp_rmem = 4096 87380 8388608 
net.ipv4.tcp_wmem = 4096 87380 8388608 
net.ipv4.tcp_keepalive_time = 1200 
net.ipv4.tcp_keepalive_intvl = 60 
net.ipv4.tcp_keepalive_probes = 3 
vm.swappiness = 0 
net.ipv4.ip_local_port_range = 1024    65535
fs.file-max=65535
net.ipv4.tcp_fin_timeout = 30 
net.ipv4.tcp_tw_recycle = 1
net.ipv4.ip_local_port_range = 1024 65000
net.ipv4.tcp_max_syn_backlog = 65536 
net.ipv4.tcp_max_tw_buckets = 20000
net.ipv4.route.gc_timeout = 100
net.ipv4.tcp_synack_retries = 1
net.core.somaxconn = 65535 
net.core.netdev_max_backlog = 262144
net.ipv4.tcp_timestamps = 0
net.ipv4.tcp_max_orphans = 262144
net.ipv4.conf.all.arp_notify = 1
fs.file-max = 1020000
net.netfilter.nf_conntrack_max = 1020000
net.nf_conntrack_max = 1020000
net.ipv4.ip_local_reserved_ports = 8000-9000,11211,6379,6389,6399,6400
EOF
sysctl -p

for name in postfix ip6tables iptables;do chkconfig $name off;service $name stop ;done

cp /etc/ssh/sshd_config{,.$(date +%F)}
sed -i 's#\#Port 22#Port 36000#g' /etc/ssh/sshd_config
sed -i 's#GSSAPIAuthentication yes#GSSAPIAuthentication no#g' /etc/ssh/sshd_config
sed -i 's#GSSAPICleanupCredentials yes#GSSAPICleanupCredentials no#g' /etc/ssh/sshd_config
sed -i 's#\#UseDNS yes#UseDNS no#g' /etc/ssh/sshd_config

for n in sshd crond rsyslog network sysstat irqbalance ;do chkconfig $n on;service $n restart ;done



