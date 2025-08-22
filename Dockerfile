FROM python:3.13-slim

ARG VERSION

COPY dist/prom433-$VERSION.tar.gz /

RUN apk add gcc
RUN pip install /prom433-$VERSION.tar.gz --extra-index-url https://www.piwheels.org/simple

ENTRYPOINT ["prom433"]
CMD []
