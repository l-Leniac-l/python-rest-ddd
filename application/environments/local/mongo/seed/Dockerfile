FROM alpine:edge

MAINTAINER lnlwd

RUN apk update \
  && apk add --no-cache mongodb-tools \
  && rm -rf /var/cache/apk/

COPY ./application/environments/local/mongo/seed/*.sh /scripts/
RUN chmod +x /scripts/*.sh

COPY ./application/environments/local/wait-for /wait-for
RUN chmod +x /wait-for

VOLUME ["/seed"]

CMD ["/bin/sh"]
