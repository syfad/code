#!/usr/bin/bash
#auth：sun_admin@126.com
##install php7 sh


php_pkg_url=http://cn2.php.net/distributions/php-7.1.0.tar.gz
pkg_path=/dmdata/install
pkg_name = 'php-7.1.0'
install_dir = '/dmdata/server/php'


yum install -y gcc gcc-c++  make zlib zlib-devel pcre pcre-devel  libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libxml2 libxml2-devel glibc glibc-devel glib2 glib2-devel bzip2 bzip2-devel ncurses ncurses-devel curl curl-devel e2fsprogs e2fsprogs-devel krb5 krb5-devel openssl openssl-devel openldap openldap-devel nss_ldap openldap-clients openldap-servers  libmcrypt libmcrypt-devel  libXpm-devel
yum install -y php-mcrypt libmcrypt libmcrypt-devel wget

cd $pkg_path
wget $php_pkg_url
if [ $? -eq 0 ];then
    echo "####下载源码成功...."
else
    echo "####下载失败，检查url"
    exit 1
fi
tar -zxvf $pkg_name.tar.gz
cd $pkg_name
./configure --prefix=/dmdata/server/php --with-config-file-path=/dmdata/server/php/etc --with-fpm-user=www --with-fpm-group=www --with-mysql=mysqlnd --with-mysqli=mysqlnd --with-pdo-mysql=mysqlnd --with-iconv-dir=/usr/local --with-openssl --enable-fpm --enable-sockets --enable-sysvsem --enable-sysvmsg --enable-shmop --enable-sysvshm --enable-mbstring --with-freetype-dir --with-jpeg-dir --with-png-dir --with-zlib --with-zlib-dir --with-libxml-dir --enable-xml --with-mhash --with-mcrypt --with-bz2 --with-curl --enable-zip --enable-ftp --with-gd --enable-bcmath --with-iconv --enable-pcntl --enable-gd-native-ttf --enable-opcache --enable-mbregex --enable-session --without-pear --enable-soap --with-gettext --with-xmlrpc --enable-inline-optimization --enable-exif --enable-maintainer-zts
if [`echo` $? != 0]; then
    exit 1
else
    `make` && `make install`

cp $pkg_path/$pkg_name/php.ini-production /dmdata/server/php/etc/php.ini
cp $pkg_path/$pkg_name/sapi/fpm/init.d.php-fpm /etc/rc.d/init.d/php-fpm
chmod +x /etc/rc.d/init.d/php-fpm
chkconfig php-fpm on
