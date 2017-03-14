# dockerfiles (deployment)
This project includes all dockerfiles for the deployment of the schul-cloud and its services.

Every service has its own `docker-compose.yml` in the included sub-directory or the accumulated `docker-compose.yml` in the root folder.

## Schul-Cloud
#### Server
- Add your secrets to the `docker-compose.yml` including:
  - SMTP
  - ACCESS_KEY_ID
  - SECRET_ACCESS_KEY
  - ENDPOINT_URL

#### Client
- Change the Server of production in the `config.js` found in `schulcloud/client/config.js` to your Host name
- Rebuild the project with docker and push it to the public docker registry

#### NGINX
- Change the Server_Name to your Host name or where the service can be found in the `cloud` file which can be found in `schulcloud/nginx/cloud`
- Rebuild the project with docker and push it to the public docker registry

## Content-Service
#### Crawler
- Change API-Keys for YouTube and Antares in the `docker-compose.yml` otherwise only 2 crawler will work

## Calendar-Service
- Nothing to change here yet...

## Notification-Service
- **WIP**

# Kubernetes
This project also includes converted [kubernetes](https://github.com/kubernetes/kubernetes) files from the main `docker-compose.yml`.
These files are converted using the [kompose tool](https://github.com/kubernetes-incubator/kompose).

>Advice: Instead of converting the `docker-compose.yml` to kubernetes compatible files again, just change the according things in the files itself.
