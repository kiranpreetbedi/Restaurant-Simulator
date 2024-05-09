admin
 - user: root
 - email: root@root.com
 - pass: root

virtualenv -p /usr/bin/python3 env


## to create new env
cd  ~/project
python3 -m venv env or python3 -m virtualenv env

## to enter virtual env
cd  ~/project
source env/bin/activate

## to exit the  virtual env
deactivate

## pre migrations steps
cd  ~/project
source env/bin/activate
pip3 freeze > requirements.txt
deactivate

# migration to new machine
cd  ~/project
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

# create new project
pip3 install django
cd  ~/project
django-admin startproject {your_project_name}
cd {your_project_name}

# to run server
cd  ~/project
python3 manage.py runserver or python3 manage.py runserver 0.0.0.0:8000
nohup python3 manage.py runserver 0.0.0.0:8000 &

# build db
python3 manage.py makemigrations
python3 manage.py migrate

# create new admin
cd  ~/project
python3 manage.py createsuperuser


## important points to remember - 
   
   - there is no absolute path present in your project folder(which is present parallel to env dir) but env have abosulte path to files and binary
   
   - while migration to new machine
      - only the project folder with requirements.txt exluding the env virtual dir
   
   - before running freeze, be sure your binary path is correct, else it will give you system packages list instead of your virtual env packages


## QnA - 

# why virtual env?
 - to limit code mistakes if any while working on project
 - to take account of dependencies and keeping version intact ac ross the machines
 - to keep it light weight and portable




### usefull commands

sudo apt install python3
pip3 install --upgrade virtualenv --break-system-packages
