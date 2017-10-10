#!/usr/bin/env bash

git init
git remote add origin https://github.com/gemetalreg/DjangoMailRu.git
git pull origin master

web=/home/box/web

if [[ !(-e ${web}) ]]
then
    mkdir -p ${web}
fi

touch ${web}/empty.txt

mkdir -p ${web}/{public,uploads,etc}
mkdir -p ${web}/public/{img,css,js}

touch ${web}/{public/empty.txt,uploads/empty.txt,etc/empty.txt}
touch ${web}/public/{img/empty.txt,css/empty.txt,js/empty.txt}

cp -f /etc/nginx/nginx.conf /home/box/web/etc/nginx.conf

git clone https://github.com/gemetalreg/DjangoMailRu.git /home/box/web

cd /home/box/web
django-admin startproject ask
cd ask
python manage.py startapp qa

bash /home/box/web/init.sh

