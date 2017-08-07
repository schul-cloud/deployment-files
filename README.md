
# dockerfiles (deployment)
---
> <span style="color:red">This repository only contains deployment files and is not meant for development.</span>
---
This project includes all dockerfiles for the deployment of the schul-cloud and its services.

For further information on docker, docker-compose, and docker-swarm, please visit their [documentation](https://docs.docker.com/).

Every service has its own `docker-compose.yml` in the included sub-directory or the accumulated `docker-compose.yml` in the root folder.

## Schul-Cloud
#### Server
For the initial running of the server no secrets are needed, but as in every project there are sometimes secrets you need for extra services such as E-Mail (SMTP) or our Storage Endpoint (AWS S3).

> Soon as environment variable again for easier secret handling

- Add your secrets to the `secrets.json`, which can be found in `schulcloud/server` including:
  - SMTP
	  - example: "smtps://genericaccount@gmail.com:genericpassword@smtp.gmail.com"
  - ACCESS_KEY_ID
	  - example: "genericstring"
  - SECRET_ACCESS_KEY
	  - exampe: "genericstring"
  - ENDPOINT_URL
	  - example: "https://genericurl.com"
  - AUTHENTICATION
	  - example: "verylonggenericstring"

---
(optional) | For further configurations please edit the `production.json`, which can be found in `schulcloud/server`.

> Soon as environment variable again for easier config handling

- mongodb:
	- can be adjusted to the uri of your mongodb including the username:password or let it only talk through the docker network to your mongodb.
	- example: "mongodb://mongodbsc:27017:schulcloud"
- services:
	- here you are able to edit the endpoints to the specific services, such as content, calendar or notification.

#### Client
- Change the BACKEND_URL in the `docker-compose.yml`, which can be found in either `schulcloud/client` or the main folder of this repository, to your appropriate host name and port number.
	- example: "https://schul-cloud.org:8080"

#### NGINX
- Change every server_name to your host name in the `cloud` file which can be found in `schulcloud/nginx/cloud`
	- example: "localhost" or "schul-cloud.org"
- Change in the `docker-compose.yml` the NGINX_HOST to the same host name as to which you have choosen in the earlier step of NGINX already.
> This should currently make no difference, but in the future the configuration might be dynamically generated on start up.

## Content-Service
### Deprecated as a new content service is on its way

## Calendar-Service
- Change the `POSTGRES_PASSWORD` and `DB_PASSWORD` in the `docker-compose.yml` to your liking.

## Notification-Service
- As currently only [firebase](https://firebase.google.com/) is supported, change the `serverToken` in `notification/service/config.json`.
	- example: "verylonggenericstring"

---
(optional) | For further configurations please edit the `production.json`, which can be found in `notification/service`.

- mongodb:
	- can be adjusted to the uri of your mongodb including the username:password or let it only talk through the docker network to your mongodb.
	- example: "mongodb://mongodbsc:27017:schulcloud"

# Kubernetes
This project also includes converted [kubernetes](https://github.com/kubernetes/kubernetes) files from the main `docker-compose.yml`.
These files are converted using the [kompose tool](https://github.com/kubernetes-incubator/kompose).

- These kubernetes files are specially made for azure
- Add your StorageAccount to the `kubernetes/storage-creator.yaml`

>Advice: Instead of converting the `docker-compose.yml` to kubernetes compatible files again, just change the according things in the files itself.
