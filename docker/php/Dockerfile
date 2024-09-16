FROM centos:7

MAINTAINER sun_admin@126.com

RUN yum install -y epel-release
RUN yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm
RUN yum install -y yum install yum-utils
RUN yum-config-manager --enable remi-php71 && sudo yum update
RUN yum -y install php71
RUN yum -y install php71-php-fpm php71-php-gd php71-php-json php71-php-mbstring php71-php-mysqlnd php71-php-xml php71-php-xmlrpc php71-php-opcache

Add start.sh /start.sh
RUN chmod +x /start.sh

CMD /start.sh

#docker build -t 192.168.100.200:80/library/php71:v1 .
#docker push 192.168.100.200:80/library/php71:v1
#RUN echo "<?php phpinfo()?>" > /var/www/html/index.php
