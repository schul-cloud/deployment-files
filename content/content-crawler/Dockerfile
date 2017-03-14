FROM node:7

WORKDIR ~/
RUN apt-get update && apt-get install -y git && git clone https://github.com/schulcloud/schulcloud-content-crawler.git
WORKDIR schulcloud-content-crawler
RUN mv config.js.example config.js
RUN npm install
EXPOSE 8091
CMD NODE_ENV=production npm start
