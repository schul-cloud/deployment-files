FROM node:7

WORKDIR ~/
RUN apt-get update && apt-get install -y git && git clone https://github.com/schulcloud/schulcloud-content-api.git
WORKDIR schulcloud-content-api
RUN npm install
EXPOSE 8090
CMD NODE_ENV=production npm start
