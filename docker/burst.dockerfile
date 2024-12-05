FROM alpine:latest
WORKDIR /usr/src/app
COPY python/ ./

RUN apk add --update --no-cache \
        bash \
        tcpdump \
        iperf \
        busybox-extras \
        iproute2 \
        iputils \
        python3

CMD ["python3", "burst.py"]