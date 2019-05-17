FROM centos:7

MAINTAINER sun_admin@126.com

ENV DOC_ROOT=/usr/local/nginx/conf/ \
    WEB_SERVER_PACKAGE="nginx-1.15.9.tar.gz"

COPY nginx.conf ${DOC_ROOT}
#COPY yum.repos.d /etc/yum.repos.d/

#项目标镜像打包文件,如果使用下面方法，直接解压.gz到目标文件夹
ADD http://nginx.org/download/${WEB_SERVER_PACKAGE} /usr/local/src/

# running required command
RUN yum install -y gcc gcc-c++ glibc make autoconf openssl openssl-devel
RUN yum install -y libxslt-devel -y gd gd-devel GeoIP GeoIP-devel pcre pcre-devel
RUN useradd -M -s /sbin/nologin nginx

#php71安装
RUN yum install -y epel-release
RUN yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm
RUN yum install -y yum install yum-utils
RUN yum-config-manager --enable remi-php71
RUN yum -y install php71
RUN yum -y install php71-php-fpm php71-php-gd php71-php-json php71-php-mbstring php71-php-mysqlnd php71-php-xml php71-php-xmlrpc php71-php-opcache

#VOLUME 指定挂在目录
#VOLUME /data/mysql

RUN cd /usr/local/src && \
    tar -zxf ${WEB_SERVER_PACKAGE} && \
    mv nginx-1.15.9 nginx

#设置工作目录，之后复制可以使用./ 便可以复制到工作目录
WORKDIR /usr/local/src/nginx
#ADD ${WEB_SERVER_PACKAGE} ./

RUN ./configure --user=nginx --group=nginx \
    --prefix=/usr/local/nginx --with-file-aio \
    --with-http_ssl_module --with-http_realip_module \
    --with-http_addition_module --with-http_xslt_module \
    --with-http_image_filter_module --with-http_geoip_module \
    --with-http_sub_module --with-http_dav_module \
    --with-http_flv_module --with-http_mp4_module \
    --with-http_gunzip_module --with-http_gzip_static_module \
    --with-http_auth_request_module --with-http_random_index_module \
    --with-http_secure_link_module --with-http_degradation_module \
    --with-http_stub_status_module && \
    make && make install

#EXPOSE 暴露端口
EXPOSE 80/tcp
EXPOSE 9000/tcp

Add start.sh /start.sh
RUN chmod +x /start.sh

CMD /start.sh