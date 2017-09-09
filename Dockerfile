FROM alpine:3.6

ADD . /app

WORKDIR /app

RUN apk update \
    && apk add --no-cache python3 \
    && apk add --no-cache --virtual .build-deps \
      gcc \
      libc-dev \
      linux-headers \
      python3-dev  \
    && python3 -m ensurepip \
    && rm -r /usr/lib/python*/ensurepip \
    && pip3 install --no-cache-dir --upgrade pip setuptools \
    && pip3 install -r requirements.txt \
    && apk del .build-deps \
    && rm -r /root/.cache

CMD ["gunicorn", "-b 0.0.0.0:5000", "--reload", "application:app.app"]
