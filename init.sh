#!/usr/bin/env bash

cd /home/box/web

git config --global user.email "itunereg@gmail.com"
git config --global user.name "gemetalreg"

sudo /etc/init.d/nginx stop

#sudo rm -rf /etc/nginx/sites-enabled/default
#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
#sudo /etc/init.d/nginx restart

#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart

sudo python /home/box/web/ask/manage.py runserver 0.0.0.0:80

sudo /etc/init.d/mysql restart
# mysql -u root -e "DROP DATABASE ASK"
mysql -u root -e "CREATE DATABASE myproject CHARACTER SET UTF8;"
mysql -u root -e "CREATE USER 'myprojectuser'@'localhost' IDENTIFIED BY 'password';"
mysql -u root -e "GRANT ALL PRIVILEGES ON myproject.* TO 'myprojectuser'@'localhost';"
mysql -u root -e "FLUSH PRIVILEGES;"

cd ask

python manage.py makemigrations
python manage.py migrate