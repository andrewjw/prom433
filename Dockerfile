FROM python:3.12-slim

ARG VERSION

COPY dist/prom433-$VERSION.tar.gz /

RUN apt install gcc

RUN pip install /prom433-$VERSION.tar.gz

ENTRYPOINT ["prom433"]
CMD []
