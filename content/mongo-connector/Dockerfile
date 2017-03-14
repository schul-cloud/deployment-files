FROM python:3.6-slim

RUN apt-get update && apt-get -y install curl mongodb && pip install 'mongo-connector[elastic2]'
RUN mkdir log && mkdir log/mongo-connector
WORKDIR ~/
RUN curl https://raw.githubusercontent.com/schulcloud/schulcloud-content-api/dev/mongo-connector-production.json >> ~/mongo-connector.json && \
curl https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh >> wait-for-it.sh && \
chmod +x wait-for-it.sh
RUN mkdir log && mkdir log/mongo-connector
RUN curl https://raw.githubusercontent.com/schulcloud/schulcloud-content-api/dev/scripts/create_es_index_contents_production.sh >> ~/elastic.sh && \
chmod +x ~/elastic.sh && echo "rs.initiate( { _id : \"replica\", members: [ { _id : 0, host : \"mongodb:27017\" } ] })" >> ~/init.js
RUN echo "mongo --host mongodb < ~/init.js \n~/elastic.sh\nmongo-connector -c ~/mongo-connector.json" >> ~/startup.sh && \
cat ~/startup.sh && \
chmod +x ~/startup.sh
CMD ~/startup.sh
