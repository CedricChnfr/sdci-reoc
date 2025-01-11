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
        iputils \
        iperf3 \
        python3
ENV VAR=""

# CMD ["/bin/sh"]
CMD ["node", "application.js", "--remote_ip", "127.0.0.1", "--remote_port", "8080", "--device_name", "dev1", "--send_period", "5000"]
