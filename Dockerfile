FROM python:3.12-slim

ARG VERSION

COPY dist/prom433-$VERSION.tar.gz /

RUN apt-get update && apt-get install -y gcc libffi-dev rustc

RUN pip install /prom433-$VERSION.tar.gz

RUN apt-get purge -y gcc libffi-dev rustc && apt-get autoremove -y && apt-get clean

ENTRYPOINT ["prom433"]
CMD []
