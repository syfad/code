FROM nginx

MAINTAINER sunyunfeng@360.cn

WORKDIR /etc/nginx/

COPY nginx.conf .

COPY default.conf conf.d/

RUN mkdir /data/luban

COPY dist_front.tar.gz /data/luban

EXPOSE 8360

CMD ["nginx", "-g", "daemon off;"]
