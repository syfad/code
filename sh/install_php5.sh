#!/usr/bin/bash

php_pkg_url = 'http://cn2.php.net/distributions/php-5.6.32.tar.gz'
pkg_name = 'php-5.6.32'
install_dir = '/dmdata/server/php'

yum -y install libxml2-devel bzip2-devel libmcrypt-devel mhash-devel libcurl-devel libpng-devel
yum -y install freetype-devel libjpeg-devel libmemcached m4 autoconf ImageMagick-devel unzip
wget $php_pkg_url
tar -zxvf $pkg_name.tar.gz

cd $pkg_name
./configure --prefix=/dmdata/server/php --with-config-file-path=/dmdata/server/php/etc --with-fpm-user=www --with-fpm-group=www --with-mysql=mysqlnd --with-mysqli=mysqlnd --with-pdo-mysql=mysqlnd --with-iconv-dir=/usr/local --with-openssl --enable-fpm --enable-sockets --enable-sysvsem --enable-sysvmsg --enable-shmop --enable-sysvshm --enable-mbstring --with-freetype-dir --with-jpeg-dir --with-png-dir --with-zlib --with-zlib-dir --with-libxml-dir --enable-xml --with-mhash --with-mcrypt --with-bz2 --with-curl --enable-zip --enable-ftp --with-gd --enable-bcmath --with-iconv --enable-pcntl --enable-gd-native-ttf --enable-opcache --enable-mbregex --enable-session --without-pear --enable-soap --with-gettext --with-xmlrpc --enable-inline-optimization --enable-exif --enable-maintainer-zts

if [`echo` $? != 0]; then
    exit 1
else
    `make` && `make install`

#cp $pkg_name/php.ini-production /dmdata/server/php/etc/php.ini
#cp $pkg_name/sapi/fpm/init.d.php-fpm /etc/rc.d/init.d/php-fpm
#chmod +x /etc/rc.d/init.d/php-fpm
#chkconfigphp-fpm on