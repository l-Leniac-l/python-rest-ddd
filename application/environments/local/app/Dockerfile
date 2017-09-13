FROM alpine:3.6

MAINTAINER lnlwd

ENV PACKAGES="\
  gcc \
  musl \
  linux-headers \
  build-base \
  ca-certificates \
  python3 \
  python3-dev \
"

RUN apk update \
  && apk add --no-cache $PACKAGES || \
    (sed -i -e 's/dl-cdn/dl-4/g' /etc/apk/repositories && apk add --no-cache $PACKAGES) \

  && if [[ ! -e /usr/bin/python ]];        then ln -sf /usr/bin/python3 /usr/bin/python; fi \
  && if [[ ! -e /usr/bin/python-config ]]; then ln -sf /usr/bin/python3-config /usr/bin/python-config; fi \
  && if [[ ! -e /usr/bin/idle ]];          then ln -sf /usr/bin/idle3 /usr/bin/idle; fi \
  && if [[ ! -e /usr/bin/pydoc ]];         then ln -sf /usr/bin/pydoc3 /usr/bin/pydoc; fi \
  && if [[ ! -e /usr/bin/easy_install ]];  then ln -sf /usr/bin/easy_install-3 /usr/bin/easy_install; fi \

  && python3 -m ensurepip \
  && pip3 install --no-cache-dir --upgrade pip setuptools \
  && if [[ ! -e /usr/bin/pip ]]; then ln -sf /usr/bin/pip3 /usr/bin/pip; fi

COPY ./application/environments/local/app/startup.sh /scripts/startup.sh
RUN chmod +x /scripts/startup.sh

COPY ./application/environments/local/wait-for /wait-for
RUN chmod +x /wait-for

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["/bin/sh"]
