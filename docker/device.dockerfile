FROM node:alpine
WORKDIR /usr/src/app
COPY js/ ./
COPY python/ ./

RUN npm install express
RUN apk add --update --no-cache \
        bash \
        tcpdump \
        iperf \
        busybox-extras \
        iproute2 \
        iputils \
        iperf3 \
        python3
ENV VAR=""

# CMD ["/bin/sh"]
CMD ["node", "device.js", "--local_ip", "127.0.0.1", "--local_port", "9001", "--local_name", "dev1", "--remote_ip", "127.0.0.1", "--remote_port", "8282", "--remote_name", "gwf1", "--send_period", "3000"]
