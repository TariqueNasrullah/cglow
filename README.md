# CgloW-OnlineJudge

Make sure ``docker.io``, ``rabbitmq-server`` is installed.

make sure ``rabbitmq-server`` is listening to port ``5672``

Language Requirement:  ``python3``

# Installation::

	pip3 install virtualenv
	python3 -m virtualenv projectCglow
	cd projectCglow/
	source bin/activate
	git clone https://github.com/TariqueNasrullah/cglow.git
	pip install django
	pip install celery
	pip install docker
	pip install channels


Goto 'projectCglow/cglow/contestjudger' and RUN

	docker build -t contestjudger .

Goto 'projectCglow/cglow/offlinejudger' and RUN

	docker build -t offlinejudger .

Goto 'projectCgloW/cglow' and RUN::

	python manage.py runserver

On another terminal, goto 'projectCglow/' and RUN
 
	source bin/activate
	cd cglow
	celery -A cglow worker -l info


# On your browser locate to http://127.0.0.1:8000
