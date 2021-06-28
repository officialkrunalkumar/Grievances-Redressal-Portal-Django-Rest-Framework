# GRS - DRF

Grievances Redressal Portal using Django Rest Framework.

## Getting start

To get started with the code on this repo, you need to either *clone* or *download* this repo into your machine just as shown below;

```bash
git clone https://gitlab.com/krunalkumar/grs-drf.git
```

or

```bash
git clone git@gitlab.com:krunalkumar/grs-drf.git
```
## Running the App

### Part 1: Create Database and virtualenv

### Move to project directory
```bash
$ cd dataproject-django-rest-framework
```

### Create Database
```bash
$ sudo -u postgres psql
```

```bash
postgres=# \i create.sql
```

```bash
postgres=# \q
```

### Install the virtualenv package
```bash
$ cd ..
$ pip install virtualenv
```
### Create the virtual environment
To create a virtual environment, you must specify a path. You may provide any name in the place of <mypython>:
```bash
$ virtualenv <venv>
```
  
### Activate the virtual environment
```bash
$ source <venv>/bin/activate
```

Now you can load the requirements.txt.
## Dependencies

Before running the application, you need to have some packages preinstalled. So I have provided all the required packages and their versions in requirements.txt file by running the below command you will be able to install all the packages.

```bash
$ cd grs-drf
$ pip install -r requirements.txt
```

#### Part 2: creating and accessing admin operations create superuser

```bash
cd ..
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
##### Note: provide your username and password in required place to create admin user.

#### Part 3: Running the application on server

```bash
$ python3 manage.py runserver

```

you can create the user by visiting admin page at ```http://127.0.0.1:8000/admin```

Now you can access the app on your local server but for performing operation in browser you need to provide the username and password of user created.

you can access the assignments api page through ```http://127.0.0.1:8000/Complaint/```
#### part 4: Postman
## Install postman
```bash
sudo snap install postman
```
## Import collection ##
1. goto to import

you can see the import option in your work space, click that and drop the file
**GRS REST API (Token Auth).postman_collection.json** and **GRS REST API.postman_collection.json**in that.

## Global variable ##

you need to set a global variable 

* VARIABLE - baseUrl
* INITIAL VALUE - http://localhost:8000
* CURRENT VALUE - http://localhost:8000

## API Authentication ##

To submit or view an order, you need to Authenticate.

You can login by both ways such as Basic Authentication and Token Authentication.

1. Basic Authentication:
In postman select basic auth in authorization and provide the provide the username 
and password of the registered user.  

2. Token Authentication:
    
POST `/api-token-auth/`
    
The request body needs to be in JSON format and include the following properties:
- `username` - String
- `password` - String
    
Example
```
{
    "username": "your_username",
    "password": "your_password"
}
```

you will get a token - yourusertoken

Now select headers then, create a key called "Authorization" and a value 
called "Token yourusertoken"

NOTE: you need to provide authentication for each request.

## Run collection ##
Now you will be able to run the collection for testing.

### Deactivate the virtual environment
To deactivate virtual environment, run
```bash
$ deactivate

```
### Delete Database
```bash
$ sudo -u postgres psql
```

```bash
postgres=# \i delete.sql
```

```bash
postgres=# \q
```