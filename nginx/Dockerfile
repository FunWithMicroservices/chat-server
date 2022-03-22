FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./django-proxy.conf /etc/nginx/conf.d
