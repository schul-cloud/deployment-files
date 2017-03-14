FROM node:7

WORKDIR ~/
RUN apt-get update && apt-get install -y git postgresql-client python-psycopg2 && git clone https://github.com/schulcloud/schulcloud-calendar.git
WORKDIR schulcloud-calendar
RUN npm install
EXPOSE 3000
COPY check.py check.py
RUN echo "#!/bin/sh\nNODE_ENV=production DB_USERNAME=node DB_HOST=postgres DB_PORT=5432 DB_DATABASE=schulcloud_calendar npm start" >> start.sh && chmod +x start.sh && \
echo "psql -h postgres -d schulcloud_calendar -U node -a -f schema.sql" >> database.sh && chmod +x database.sh
CMD python check.py
