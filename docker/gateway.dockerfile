FROM node:alpine
WORKDIR /usr/src/app
COPY js/ ./

RUN npm install express
RUN apk add --update --no-cache \
        bash \
        tcpdump \
        iperf \
        busybox-extras \
        iproute2 \
        iperf3 \
        iputils
ENV VAR=""

# CMD ["/bin/sh"]
CMD ["node", "gateway.js", "--local_ip", "127.0.0.1", "--local_port", "8181", "--local_name", "gwi", "--remote_ip", "127.0.0.1", "--remote_port", "8080", "--remote_name", "srv"]
