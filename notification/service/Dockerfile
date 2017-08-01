FROM node:7

WORKDIR ~/
RUN apt-get update && apt-get install -y git && git clone https://github.com/schul-cloud/node-notification-service.git
WORKDIR node-notification-service
RUN git checkout schulcloud-compatible && \
npm install
COPY config.json secure/config.json
COPY production.json config/production.json
EXPOSE 3030
CMD npm start
