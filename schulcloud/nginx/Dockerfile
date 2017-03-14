FROM nginx:1.11.10

COPY cloud /etc/nginx/conf.d/cloud.conf
EXPOSE 80 8080

CMD ["nginx", "-g", "daemon off;"]
