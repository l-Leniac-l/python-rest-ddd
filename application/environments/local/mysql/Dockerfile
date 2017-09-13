FROM alpine:3.6

MAINTAINER lnlwd

RUN apk update \
  && apk add --no-cache mysql mysql-client \

  && addgroup mysql mysql \
  && mkdir /scripts \
  && rm -rf /var/cache/apk/

VOLUME ["/var/lib/mysql"]

COPY ./application/environments/local/mysql/*.sh /scripts/
RUN chmod +x /scripts/*.sh

COPY ./application/environments/local/mysql/my.cnf /etc/mysql/my.cnf

EXPOSE 3306

ENTRYPOINT ["/scripts/startup.sh"]
