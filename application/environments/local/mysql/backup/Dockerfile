FROM alpine:3.6

MAINTAINER lnlwd

RUN apk update \
  && apk add --no-cache mysql-client tar\
  && rm -rf /var/cache/apk/

COPY ./application/environments/local/mysql/backup/*.sh /scripts/
RUN chmod +x /scripts/*.sh

COPY ./application/environments/local/wait-for /wait-for
RUN chmod +x /wait-for

VOLUME ["/backup"]

CMD ["/bin/sh"]
