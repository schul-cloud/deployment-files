FROM node:7

WORKDIR ~/
RUN apt-get update && apt-get install -y git && git clone https://github.com/schulcloud/schulcloud-client.git
WORKDIR schulcloud-client
RUN npm install && \
npm install -g nodemon gulp
RUN gulp
EXPOSE 3100
CMD BACKEND_URL=http://server:8080 node bin/www
