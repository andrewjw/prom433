FROM python:3.10-slim

ARG VERSION

RUN apt-get update; \
	apt install -y software-properties-common; \
	add-apt-repository universe; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		rtl_433 \
	; \
	rm -rf /var/lib/apt/lists/* && \
    pip install prom433==$VERSION

ENTRYPOINT ["prom433"]
CMD []
