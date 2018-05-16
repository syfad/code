#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21
# @Author  : sunyf (sunyfad@gmail.com)
# @Disc    : install Nginx
# @Disc    : support python 2.x and 3.x

#安装参数需要手动添加openssl源码路径“--with-openssl=/dmdata/install/openssl-1.0.2n”

import os
import sys
# import getopt
# import filecmp

if os.getuid() == 0:
    pass
else:
    print "当前用户不是root，请切换为root"
    sys.exit(1)

nginx_pkg_url = 'http://nginx.org/download/nginx-1.14.0.tar.gz'
pkg_name = 'nginx-1.14.0'
install_dir = '/dmdata/server/nginx'

work_path = os.getcwd()
#print work_path

def install_nginx():
    print "####检查安装目录......"
    if os.path.exists(install_dir):
        print(install_dir+ "已存在nginx目录，请确认")
        sys.exit(1)
    print("####安装目录正常......")

    print('####yum安装依赖包')
    cmd = "yum install gcc gcc-c++ zlib zlib-devel openssl openssl-devel pcre-devel pcre automake autoconf libtool make -y"
    os.system("yum -y install pcre-devel")
    res = os.system(cmd)
    if res !=0:
        print('yum安装失败，请检查环境')
        sys.exit(1)

    print('添加nginx用户')
    cmd = 'useradd -s /sbin/nologin -M nginx'
    res = os.system(cmd)
    if res !=0:
        print('nginx已存在，请检查')

    print('####下载安装包......')
    cmd = 'wget ' + nginx_pkg_url
    res = os.system(cmd)
    if res !=0:
        print('下载源码失败，请检查当前网络')
        sys.exit(1)

    print('####解压安装包......')
    cmd = 'tar -zxvf' +pkg_name+'.tar.gz'
    res = os.system(cmd)
    if res !=0:
        os.system('rm' +pkg_name+'.tar.gz')
        print('解压失败，重新运行此脚本下载。')
        sys.exit(1)

    #os.chdir(pkg_name)
    print('####编译安装nginx......')
    cmd = 'cd  ' +pkg_name+ '&& ./configure --prefix=/dmdata/server/nginx --user=nginx --group=nginx --with-http_ssl_module --with-http_flv_module --with-http_stub_status_module --with-http_gzip_static_module --http-client-body-temp-path=/var/tmp/nginx/client --http-proxy-temp-path=/var/tmp/nginx/proxy --http-fastcgi-temp-path=/var/tmp/nginx/fcgi --http-uwsgi-temp-path=/var/tmp/nginx/uwsgi --http-scgi-temp-path=/var/tmp/nginx/scgi --with-pcre --with-openssl=/dmdata/install/openssl-1.0.2n && make && make install'
    res = os.system(cmd)
    if res !=0:
        os.system('rm -f ' +pkg_name+'.tar.gz')
        os.system('rm -rf ' +pkg_name)
        print('编译安装nginx失败，请检查安装相关依赖库,并重新运行此脚本安装......')
        sys.exit(1)

if __name__ == '__main__':
    install_nginx()
