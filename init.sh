#!/usr/bin/env bash

mkdir -p /home/box/web/{public,uploads,etc}
mkdir -p /home/box/web/public/{img,css,js}

empty = "empty.txt"
touch /home/box/web/{public/$(empty),uploads/$(empty),etc/$(empty)}
touch /home/box/web/public/{img/$(empty),css/$(empty),js/$(empty)}

cp -pf /etc/nginx/nginx.conf /home/box/web/etc/nginx.conf

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
