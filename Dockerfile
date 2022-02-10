FROM python:3.10-slim

ARG VERSION

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
		rtl-433 \
	&& \
	rm -rf /var/lib/apt/lists/* && \
    pip install prom433==$VERSION

ENTRYPOINT ["prom433"]
CMD []
