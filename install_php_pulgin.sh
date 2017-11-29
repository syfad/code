#!/usr/bin/bash 

echo "####安装memcache....."
sleep 1
mem_name='memcache-3.0.8'
wget 'https://pecl.php.net/get/memcache-3.0.8.tgz'
if [ $? -eq 0 ];then
    echo "####下载源码成功...."
else
    echo "####下载失败，检查url"
    exit 1
fi

/bin/tar zxvf ${mem_name}.tgz
if [ $? -eq 0 ];then
    echo "##tar sucess"
else
    echo "####解压失败"
    exit 1
fi
cd $mem_name
/dmdata/server/php/bin/phpize
yum -y install libmemcached
if [ $? -eq 0 ];then
    echo "####安装libmemcached成功...."
else
    exit 1
fi

./configure --enable-memcached --with-php-config=/dmdata/server/php/bin/php-config
if [ $? -eq 0 ];then
    echo "####编译成功，开始安装...."
    make && make install
else
    exit 1
fi

#vim /usr/local/php/etc/php.ini
#extension_dir = "/usr/local/php-5.6.9/lib/php/extensions/no-debug-zts-20131226/"
#extension = memcache.so
#重启php-fpm
#service php-fpm reload

echo "#################################################安装mongodb扩展....."
sleep 2
Mongo_Name='mongo-1.6.8'
wget 'http://pecl.php.net/get/mongo-1.6.8.tgz'
if [ $? -eq 0 ];then
    echo "####下载完成...."
    sleep 2
else
    exit 1
fi

tar zxvf ${Mongo_Name}.tgz
if [ $? -eq 0 ];then
    echo "##tar sucess"
else
    echo "####解压失败"
    exit 1
fi
cd $Mongo_Name
/dmdata/server/php/bin/phpize
./configure --with-php-config=/dmdata/server/php/bin/php-config
if [ $? -eq 0 ];then
    echo "####编译完成...."
    sleep 2
else
    exit 1
fi
make && make install
if [ $? -eq 0 ];then
    echo "####编译安装完成...."
    sleep 2
else
    exit 1
fi

#vim /usr/local/php/etc/php.ini
#extension_dir = "/usr/local/php-5.6.9/lib/php/extensions/no-debug-zts-20131226/"
#extension = mongo.so
#重新php-fpm
#service php-fpm reload

echo "#################################################安装phalcon扩展....."
sleep 2
yum -y install git
git clone 'git://github.com/phalcon/cphalcon.git'
if [ $? -eq 0 ];then
    echo "##clone sucess"
else
    echo "####clone phalcon 源码失败"
    exit 1
fi
cd cphalcon/build/php5/64bits/
/dmdata/server/php/bin/phpize
./configure --with-php-config=/dmdata/server/php/bin/php-config
if [ $? -eq 0 ];then
    echo "##编译成功"
else
    echo "####编译失败"
    exit 1
fi
make && make install
if [ $? -eq 0 ];then
    echo "##编译安装成功"
else
    echo "####phalcon扩展编译安装失败"
    exit 1
fi
#vim /usr/local/php/etc/php.ini
#extension_dir = "/usr/local/php-5.6.9/lib/php/extensions/no-debug-zts-20131226/"
##extension = phalcon.so
#重新php-fpm
#service php-fpm reload


echo "#################################################安装redis扩展....."
sleep 2
Redis_Name='redis-2.2.7'
wget 'http://pecl.php.net/get/redis-2.2.7.tgz'
if [ $? -eq 0 ];then
    echo "##download成功"
else
    echo "####下载redis扩展失败"
    exit 1
fi

tar zxvf ${Redis_Name}.tgz
if [ $? -eq 0 ];then
    echo "##tar 成功"
else
    echo "####tar 失败"
    exit 1
fi
cd $Redis_Name
if [ $? -eq 0 ];then
    echo `pwd`
else
    echo "####cd path失败"
    exit 1
fi

/dmdata/server/php/bin/phpize
./configure --with-php-config=/dmdata/server/php/bin/php-config
if [ $? -eq 0 ];then
    echo "##编译安装成功"
else
    echo "####redis扩展编译安装失败"
    exit 1
fi

make && make install
if [ $? -eq 0 ];then
    echo "##编译安装成功"
else
    echo "####redis扩展编译安装失败"
    exit 1
fi

#vim /dmdata/server/php/etc/php.ini
#extension = redis.so
