FROM nginx:latest
LABEL maintainer="shun850211@gmail.com"


COPY nginx.conf /etc/nginx/nginx.conf
COPY shop.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/ && \
    ln -s /etc/nginx/sites-available/shop.conf /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]
