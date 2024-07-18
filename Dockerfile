# syntax = docker/dockerfile:experimental
FROM python:3.12-slim

ARG VERSION

COPY dist/prom433-$VERSION.tar.gz /

# Workaround for building cryptographic Python package on arm/v7 images.
# https://github.com/docker/buildx/issues/395
RUN --security=insecure mkdir -p /root/.cargo && chmod 777 /root/.cargo && mount -t tmpfs none /root/.cargo &&

RUN apt-get update && apt-get install -y gcc libffi-dev rustc

RUN pip install /prom433-$VERSION.tar.gz

RUN apt-get purge -y gcc libffi-dev rustc && apt-get autoremove -y && apt-get clean

ENTRYPOINT ["prom433"]
CMD []
