FROM alpine:3.15.0

ARG VERSION

RUN apk add python3 py3-pip && \
    apk add rtl_433 --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/ && \
    pip install prom433==$VERSION

ENTRYPOINT ["prom433"]
CMD []
