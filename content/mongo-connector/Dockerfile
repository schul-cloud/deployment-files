FROM python:3.6.1

# Install Required Python Modules
RUN pip install mongo-connector && pip install elastic2-doc-manager[elastic5]

WORKDIR ~/
RUN mkdir log && mkdir log/mongo-connector && \
wget https://raw.githubusercontent.com/schul-cloud/schulcloud-content/master/mongo-connector-production.json

# TODO: Set mongodb in replica state
# chmod +x ~/elastic.sh && echo "rs.initiate( { _id : \"replica\", members: [ { _id : 0, host : \"mongodb:27017\" } ] })" >> ~/init.js

CMD "mongo-connector -c ~/mongo-connector-production.json"
