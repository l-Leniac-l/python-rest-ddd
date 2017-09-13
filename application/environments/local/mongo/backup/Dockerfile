FROM alpine:edge

MAINTAINER lnlwd

RUN apk update \
  && apk add --no-cache mongodb-tools tar\
  && rm -rf /var/cache/apk/

COPY ./application/environments/local/mongo/backup/*.sh /scripts/
RUN chmod +x /scripts/*.sh

COPY ./application/environments/local/wait-for /wait-for
RUN chmod +x /wait-for

VOLUME ["/backup"]

CMD ["/bin/sh"]
