FROM alpine:latest

RUN apk add --update --no-cache \
        bash \
        tcpdump \
        iperf \
        busybox-extras \
        iproute2 \
        iperf3 \
        iputils

CMD ["/bin/bash"]