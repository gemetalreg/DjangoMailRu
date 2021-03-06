# install nginx
# main: /etc/nginx/{nginx.conf|sites-available}
sudo apt-get update
sudo apt-get install nginx

# create folders
mkdir -p /home/box/web/public /home/box/web/uploads /home/box/web/etc
mkdir -p /home/box/web/public/img /home/box/web/public/css /home/box/web/public/js

# create weak link to sites-enabled
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/conf.d/test.conf

# delete default virtual host
sudo rm -f /etc/nginx/sites-enabled/default

# create weak link gunicorn conf named hello.py
# sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py

# run nginx
sudo /etc/init.d/nginx restart

# run gunicorn
sudo gunicorn --chdir /home/box/web -c /home/box/web/etc/hello.py hello:app
