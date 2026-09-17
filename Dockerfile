FROM python:3.12-slim AS builder
LABEL org.opencontainers.image.authors="Josh Rhoades <josh@axds.co>"

LABEL org.opencontainers.image.licenses="MIT"

ENV PROJECT_ROOT=/opt/docs

RUN apt-get update && apt-get install -y make && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir uv

RUN useradd --create-home docuser

COPY --chown=docuser:docuser requirements.txt /tmp/requirements.txt
RUN uv pip install --system -r /tmp/requirements.txt && rm /tmp/requirements.txt

RUN mkdir -p $PROJECT_ROOT && chown -R docuser:docuser $PROJECT_ROOT

USER docuser
COPY --chown=docuser:docuser source $PROJECT_ROOT/source
COPY --chown=docuser:docuser Makefile $PROJECT_ROOT/

WORKDIR $PROJECT_ROOT

RUN make html

FROM nginx:1.20.2
COPY --from=builder /opt/docs/build/html /usr/share/nginx/html
