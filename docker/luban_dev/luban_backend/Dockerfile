FROM 10.203.0.42:8360/luban-docker/luban-dev:v1.2.2

MAINTAINER sunyunfeng@360.cn

WORKDIR /app/luban_port/luban_port

ENV SERVER_PACKAG="dist_back.tar.gz"

COPY ${SERVER_PACKAG} /app/luban_port/luban_port

RUN tar -zxf ${SERVER_PACKAG}

RUN pip install -r /app/luban_port/luban_port/requirements.txt

EXPOSE 9002/tcp

Add start.sh /start.sh
RUN chmod +x /start.sh

CMD /start.sh