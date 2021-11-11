FROM python:3.8

ARG VERSION

RUN pip install prom433==$VERSION

ENTRYPOINT ["prom433"]
CMD []
