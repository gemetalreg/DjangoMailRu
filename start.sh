#!/usr/bin/env bash

#git init
#git remote add origin https://github.com/gemetalreg/DjangoMailRu.git
#git pull origin master

#touch /home/box/web/empty.txt

# mkdir -p /home/box/web/{public,uploads,etc}
# mkdir -p /home/box/web/public/{img,css,js}

# touch /home/box/web/{public/empty.txt,uploads/empty.txt,etc/empty.txt}
# touch /home/box/web/public/{img/empty.txt,css/empty.txt,js/empty.txt}

#cp -f /etc/nginx/nginx.conf /home/box/web/etc/nginx.conf

#git clone https://github.com/gemetalreg/DjangoMailRu.git /home/box/web

cd /home/box/web
django-admin startproject ask
cd ask
python manage.py startapp qa

#bash /home/box/web/init.sh

