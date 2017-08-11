FROM ubuntu:16.04

WORKDIR ~/
RUN apt-get update && apt-get install -y build-essential python curl git mongodb-clients && git clone https://github.com/schulcloud/schulcloud-server.git
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && apt-get install nodejs

WORKDIR schulcloud-server
RUN npm install
COPY check.py check.py
RUN echo "#!/bin/sh\nNODE_ENV=production npm start" >> start.sh && \
chmod +x start.sh && \
curl https://bootstrap.pypa.io/get-pip.py >> get-pip.py && \
python get-pip.py && \
python -m pip install pymongo && \
echo "#!/bin/sh\n./backup.sh -H mongodbsc:27017 -p setup/ -a import" >> seed.sh && \
chmod +x seed.sh
EXPOSE 9000
CMD python check.py
