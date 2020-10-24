# install nginx
# main: /etc/nginx/{nginx.conf|sites-available}
sudo apt-get update
sudo apt-get install nginx

# create folders
mkdir -p /home/box/web/public /home/box/web/uploads /home/box/web/etc
mkdir -p /home/box/web/public/img /home/box/web/public/css /home/box/web/public/js

# create weak link to sites-enabled
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

# delete default virtual host
sudo rm -f /etc/nginx/sites-enabled/default

# run nginx
nginx -s reload
