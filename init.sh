#!/usr/bin/env bash

mkdir -p /home/box/web/{public, uploads, etc}
mkdir -p /home/box/web/public/{img, css, js}

sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
