#!/usr/bin/bash

#需要安装openssl 1.0.2.j 以上

PackagePath=/dmdata/install/
Phpize=/dmdata/server/php/bin/phpize
PhpConfig=/dmdata/server/php/bin/php-config


echo "###cphalcon php框架安装###"
cd $PackagePath
git clone --depth=1 git://github.com/dreamsxin/cphalcon7.git
if [ $? -eq 0 ];then
    echo "####下载源码成功...."
else
    echo "####下载失败，检查url"
    exit 1
fi
cd cphalcon7/ext
$Phpize
./configure --with-php-config={$PhpConfig}
make && sudo make install


echo "###redis 扩展安装###"
cd $PackagePath
wget https://github.com/phpredis/phpredis/archive/php7.zip
if [ $? -eq 0 ];then
    echo "####下载源码成功...."
else
    echo "####下载失败，检查url"
    exit 1
fi
unzip php7.zip
cd phpredis-php7/
$Phpize
./configure --with-php-config={$PhpConfig}
make && make install

echo 'memcached扩展 安装libmemcached'
#php7强烈建议需要libmemcached-1.0.18版本 下载地址链接： https://launchpad.net/libmemcached/+download
cd $PackagePath
wget https://launchpadlibrarian.net/165454254/libmemcached-1.0.18.tar.gz
if [ $? -eq 0 ];then
    echo "####下载源码成功...."
else
    echo "####下载失败，检查url"
    exit 1
fi
tar zxvf libmemcached-1.0.18.tar.gz
cd libmemcached-1.0.18
./configure --prefix=/usr/local/libmemcached --with-memcached
make && make install

echo "memcached扩展 安装"
cd $PackagePath
wget https://pecl.php.net/package/memcached/memcached-3.0.2.tgz
if [ $? -eq 0 ];then
    echo "####下载源码成功...."
else
    echo "####下载失败，检查url"
    exit 1
fi
cd memcached-3.0.2
$Phpize
./configure --enable-memcached --with-php-config={$PhpConfig} --with-libmemcached-dir=/usr/local/libmemcached --disable-memcached-sasl
make && make install

echo "memcache扩展 安装..."
cd $PackagePath
wget https://github.com/websupport-sk/pecl-memcache/archive/php7.zip
if [ $? -eq 0 ];then
    echo "####下载源码成功...."
else
    echo "####下载失败，检查url"
    exit 1
fi
unzip pecl-memcache-php7.zip
cd pecl-memcache-php7
$Phpize
./configure --with-php-config={$PhpConfig}
make && make install

echo "####mongodb扩展安装#####"
cd $PackagePath
wget https://pecl.php.net/package/mongodb/mongodb-1.2.8.tgz
if [ $? -eq 0 ];then
    echo "####下载源码成功...."
else
    echo "####下载失败，检查url"
    exit 1
fi
tar -zxvf mongodb-1.2.8.tgz
$Phpize
./configure --with-php-config={$PhpConfig}
make && make install





































