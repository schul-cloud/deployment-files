FROM node:6.10.2

# Prepare non-root user and folders
RUN useradd --system --user-group --create-home app && \
    mkdir /app && chown app:app /app

# Clone Project into Container
WORKDIR /app
RUN git clone --depth=1 https://github.com/schul-cloud/schulcloud-content.git

# Install Dependencies
WORKDIR /app/schulcloud-content
RUN npm install && chown -R app:app .

USER app
WORKDIR /app/schulcloud-content

EXPOSE 4040
CMD ["npm", "start"]