#!/usr/bin/bash
#auth:SunYunfeng
#mail:sun_admin@126.com

#需要安装openssl 1.0.2.j 以上

pkg_path=/dmdata/install
Phpize=/dmdata/server/php/bin/phpize
PhpConfig=/dmdata/server/php/bin/php-config

Cphalcon=cphalcon7
Redis=redis-4.0.2
Libmemcached=libmemcached-1.0.18
Memcached=memcached-3.0.4
Mongodb=mongodb-1.4.3


echo "###cphalcon php框架安装###"
yum -y install git
cd $pkg_path
if [ ! -d $pkg_path/$Cphalcon ];then
    git clone --depth=1 git://github.com/dreamsxin/cphalcon7.git
    cd $Cphalcon/ext
else
    cd $Cphalcon/ext
fi
$Phpize
./configure --with-php-config=$PhpConfig
make && make install


echo "###redis 扩展安装###"
cd $pkg_path
#wget https://github.com/phpredis/phpredis/archive/php7.zip

if [ ! -f $pkg_path/$Redis.tgz ];then
    wget http://pecl.php.net/get/redis-4.0.2.tgz
    tar -zxvf $Redis.tgz
    cd $Redis
elif [ -d $Redis/ ];then
    cd $Redis
else
    tar -zxvf $Redis.tgz
    cd $Redis
fi
$Phpize
./configure --with-php-config=$PhpConfig
make && make install

echo '===================memcached扩展 安装libmemcached==================='
#php7强烈建议需要libmemcached-1.0.18版本 下载地址链接： https://launchpad.net/libmemcached/+download
cd $pkg_path

if [ ! -f $pkg_path/$Libmemcached.tar.gz ];then
    wget https://launchpadlibrarian.net/165454254/libmemcached-1.0.18.tar.gz
    tar zxvf $Libmemcached.tar.gz
    cd $Libmemcached
elif [ -d $Libmemcached/ ];then
    cd $Libmemcached
else
    tar -zxvf $Libmemcached.tar.gz
    cd $Libmemcached
fi
./configure --prefix=/usr/local/libmemcached --with-memcached
make && make install

echo "memcached扩展 安装"
cd $pkg_path

if [ ! -f $pkg_path/$Memcached.tgz ];then
    wget https://pecl.php.net/get/memcached-3.0.4.tgz
    tar -zxvf $Memcached.tgz
    cd $Memcached
elif [ -d $Memcached/ ];then
    cd $Memcached
else
    tar -zxvf $Memcached.tgz
    cd $Memcached
fi

$Phpize
./configure --enable-memcached --with-php-config=$PhpConfig --with-libmemcached-dir=/usr/local/libmemcached --disable-memcached-sasl
make && make install

echo "memcache扩展 安装..."
cd $pkg_path

if [ ! -f $pkg_path/php7.zip ];then
    wget https://github.com/websupport-sk/pecl-memcache/archive/php7.zip
    unzip php7.zip
    cd pecl-memcache-php7
elif [ -d "pecl-memcache-php7/" ];then
    cd pecl-memcache-php7
else
    unzip php7.zip
    cd pecl-memcache-php7
fi

$Phpize
./configure --with-php-config=$PhpConfig
make && make install

echo '############mongodb扩展安装#################'
cd $pkg_path

if [ ! -f $pkg_path/$Mongodb.tgz ];then
    wget https://pecl.php.net/get/mongodb-1.4.3.tgz
    tar -zxvf $Mongodb.tgz
    cd $Mongodb
elif [ -d $Mongodb/ ];then
    cd $Mongodb
else
    tar -zxvf $Mongodb.tgz
    cd $Mongodb
fi

$Phpize
./configure --with-php-config=$PhpConfig
make && make install

#将如下模块导入添加到/dmdata/server/php/etc/php.ini
#extension_dir = "/dmdata/server/php/lib/php/extensions/no-debug-zts-20160303/"
#extension = redis.so
#extension = phalcon.so
#extension = mongodb.so
#extension = memcached.so
#extension = memcache.so
#extension = openssl.so





