FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY . /usr/share/nginx/html

EXPOSE 8081 8082 8083 8084 8085
