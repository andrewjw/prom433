FROM python:3.12-slim

ARG VERSION

COPY dist/prom433-$VERSION.tar.gz /

RUN apt-get update && apt-get install -y gcc

RUN pip install /prom433-$VERSION.tar.gz

RUN apt-get purge -y gcc && apt-get clean

ENTRYPOINT ["prom433"]
CMD []
