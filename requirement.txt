install docker.io
install rabbitmq-server; #make sure rabbitmq-server is listening to port 5672

language python3

installation -- >

#pip3 install virtualenv
#python3 -m virtualenv projectCglow
#cd projectCglow/
#source bin/activate
#git clone https://github.com/TariqueNasrullah/cglow.git
#pip install django
#pip install celery
#pip install docker

goto projectCglow/cglow/contestjudger
RUN 
#docker build -t contestjudger .
don't forget the (.) dot

goto projectCglow/cglow/offlinejudger
RUN 
#docker build -t offlinejudger .
don't forget the (.) dot

goto projectCgloW/cglow
RUN 
#python manage.py runserver

on another terminal, goto projectCglow
RUN 
#source bin/activate
#cd cglow
#celery -A cglow worker -l info

On your browser locate to http://127.0.0.1:8000
