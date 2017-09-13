FROM alpine:edge

MAINTAINER lnlwd

RUN apk update \
  && apk add --no-cache mongodb \
  && mkdir /data && mkdir /data/db \
  && mkdir /scripts \
  && rm /usr/bin/mongoperf

VOLUME ["/data/db"]

EXPOSE 27017

COPY ./application/environments/local/mongo/startup.sh /scripts/startup.sh
RUN chmod +x /scripts/startup.sh

ENTRYPOINT [ "/scripts/startup.sh" ]
CMD [ "mongod" ]
