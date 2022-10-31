dashboard
Structure
models.py: Where all models live
views.py:  Where all views for web page live
urls.py:   Router for web pages views
admin.py  All Django admin related settings
middlewares.py All custom django middlewares 
PEP8 comapatible coding style


Tech Stack
Following is the tech stack being used for main project:

Django==3.2.6 The core Web Framework
djangorestframework==3.12.4  for Creating RestApi

postgresql- As datastore

Project Setup
sudo apt-get update
sudo apt-get install python-pip python-dev python3.8.11-dev git

sudo pip install --upgrade pip


Activate the virtualenv
. venv/bin/activate
cd testdemo pip install -r requirements.txt

python manage.py runserver