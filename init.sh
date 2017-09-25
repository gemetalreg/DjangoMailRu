#!/usr/bin/env bash

#mkdir -p /home/box/web/{public,uploads,etc}
#mkdir -p /home/box/web/public/{img,css,js}
#
#touch /home/box/web/{public/empty.txt,uploads/empty.txt,etc/empty.txt}
#touch /home/box/web/public/{img/empty.txt,css/empty.txt,js/empty.txt}

#cp -f /etc/nginx/nginx.conf /home/box/web/etc/nginx.conf

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start

#server {
#    listen 80 default;
#    location ^~ /uploads/ {
#        root /home/box/web;
#    }
#    location ~* ^.+\.\w+$ {
#        root /home/box/public;
#    }
#    location / {
#        return 404;
#    }
#}
