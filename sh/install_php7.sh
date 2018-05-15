#!/usr/bin/bash
#auth：sun_admin@126.com
##install php7 sh
#需要先安装libmcrypt-2.5.7 和升级openssl至openssl-1.0.2n
#============================================================================
#libmcrypt-2.5.7
#wget ftp://mcrypt.hellug.gr/pub/crypto/mcrypt/libmcrypt/libmcrypt-2.5.7.tar.gz
#tar -zxvf libmcrypt-2.5.7.tar.gz
#./configure --prefix=/usr/local
#make && make install
#============================================================================

#============================================================================
# wget https://www.openssl.org/source/old/1.0.2/openssl-1.0.2n.tar.gz
# yum -y install zlib
# tar -zxvf openssl-1.0.2n.tar.gz 
# ./config shared zlib
# make && make install
# mv /usr/bin/openssl /usr/bin/openssl.bak
# mv //usr/include/openssl /usr/include/openssl.bak
# ln -s /usr/local/ssl/bin/openssl /usr/bin/openssl
# ln -s /usr/local/ssl/include/openssl /usr/include/openssl
# echo "/usr/local/ssl/lib/" >> /etc/ld.so.conf
# ldconfig -v
# openssl version -a
#============================================================================

php_pkg_url=http://cn2.php.net/distributions/php-7.1.0.tar.gz
pkg_path=/dmdata/install
pkg_name='php-7.1.0'
install_dir=/dmdata/server/php


yum install -y gcc gcc-c++  make zlib zlib-devel pcre pcre-devel  libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libxml2 libxml2-devel glibc glibc-devel glib2 glib2-devel bzip2 bzip2-devel ncurses ncurses-devel curl curl-devel e2fsprogs e2fsprogs-devel krb5 krb5-devel openssl openssl-devel openldap openldap-devel nss_ldap openldap-clients openldap-servers  libmcrypt libmcrypt-devel  libXpm-devel
yum install -y php-mcrypt libmcrypt libmcrypt-devel

cd $pkg_path
if [ ! -f $pkg_path/$pkg_name.tar.gz ];then
    wget $php_pkg_url
elif [ -d $pkg_name/ ];then
    cd $pkg_name
else
    tar -zxvf $pkg_name.tar.gz
    cd $pkg_name
fi
./configure --prefix=/dmdata/server/php --with-config-file-path=/dmdata/server/php/etc --with-fpm-user=www --with-fpm-group=www  --with-mysqli=mysqlnd --with-pdo-mysql=mysqlnd --with-iconv-dir=/usr/local --with-openssl --enable-fpm --enable-sockets --enable-sysvsem --enable-sysvmsg --enable-shmop --enable-sysvshm --enable-mbstring --with-freetype-dir --with-jpeg-dir --with-png-dir --with-zlib --with-zlib-dir --with-libxml-dir --enable-xml --with-mhash --with-mcrypt --with-bz2 --with-curl --enable-zip --enable-ftp --with-gd --enable-bcmath --with-iconv --enable-pcntl --enable-gd-native-ttf --enable-opcache --enable-mbregex --enable-session --without-pear --enable-soap --with-gettext --with-xmlrpc --enable-inline-optimization --enable-exif --enable-maintainer-zts
if [ $? -eq 0 ];then
    make && make install
else
    exit 1
fi

cp $pkg_path/$pkg_name/php.ini-production /dmdata/server/php/etc/php.ini
cp $pkg_path/$pkg_name/sapi/fpm/init.d.php-fpm /etc/rc.d/init.d/php-fpm
chmod +x /etc/rc.d/init.d/php-fpm
chkconfig php-fpm on