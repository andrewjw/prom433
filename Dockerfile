FROM python:3.10-slim

ARG VERSION

RUN pip install prom433==$VERSION

ENTRYPOINT ["prom433"]
CMD []
