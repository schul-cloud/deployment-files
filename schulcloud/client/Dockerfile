FROM node:7

WORKDIR ~/
RUN apt-get update && apt-get install -y git && git clone https://github.com/schulcloud/schulcloud-client.git
WORKDIR schulcloud-client
RUN npm install && \
rm -rf src/modules/core/helpers/config.js
COPY config.js src/modules/core/helpers/config.js
RUN npm install webpack -g && NODE_ENV=production webpack -d
EXPOSE 3100
CMD NODE_ENV=production node server.js
