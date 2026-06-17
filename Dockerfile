FROM nginx:alpine

COPY index.html /usr/share/nginx/html/
COPY *.svg /usr/share/nginx/html/
COPY slideshow.html /usr/share/nginx/html/

COPY nginx.conf /etc/nginx/nginx.conf

