#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21
# @Author  : sunyf (sunyfad@gmail.com)
# @Disc    : install Nginx
# @Disc    : support python 2.x and 3.x

import os
import sys
# import getopt
# import filecmp

if os.getuid() == 0:
    pass
else:
    print "当前用户不是root，请切换为root"
    sys.exit(1)

nginx_pkg_url = 'https://openresty.org/download/openresty-1.9.15.1.tar.gz'
pkg_name = 'openresty-1.9.15.1'
install_dir = '/dmdata/server/openresty'

work_path = os.getcwd()
#print work_path

def install_openresty():
    print "####检查安装目录......"
    if os.path.exists(install_dir):
        print(install_dir+ "已存在openresty目录，请确认")
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
    print('####编译安装openresty......')
    cmd = 'cd  ' +pkg_name+ '&& ./configure --prefix=/dmdata/server/openresty --user=nginx --group=nginx --with-http_v2_module --with-http_sub_module --with-http_stub_status_module --with-luajit && make && make install'
    res = os.system(cmd)
    if res !=0:
        os.system('rm -f ' +pkg_name+'.tar.gz')
        os.system('rm -rf ' +pkg_name)
        print('编译安装openresty失败，请检查安装相关依赖库,并重新运行此脚本安装......')
        sys.exit(1)

if __name__ == '__main__':
    install_openresty()
