# [Insta_Gram](https://markozy-insta.herokuapp.com/)

This is an attempt at cloning the social media site instagram where users share comment and like photos

## Author

* **Marcus Jean-Louis**  [Marcusjnls](https://github.com/Marcusjnls)

## Getting Started

Fork this repository or clone it to your local machine running Ubuntu by using the following commands:
```
git clone (https://github.com/Marcusjnls/instagram-clone.git)
```

### Prerequisites

You will need to be running the following:

* Python version 3.6
* postgres database

### Installing

A step by step series of examples that tell you how to get a development env running

* set up a virtual environment using the following command
```
python3.6 -m venv --without-pip virtual
```

And activate it

```
source virtual/bin/activate
```
* install the latest version of pip

```
curl https://bootstrap.pypa.io/get-pip.py | python
```

* Install the requirements in the requirements.txt file using
```
pip install -r requirements.txt
```

* create a .env file in your rootfolder and add the following configurations
```
SECRET_KEY='<random-string>'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='postgres://databaseowner:password@localhost/databasename'
```

* create postgres database
```
CREATE DATABASE <your-database-name>
```

* create a migration using the following command
```
python3.6 manage.py makemigrations
```

and migrate

```
python3.6 manage.py migrate
```

* create an admin account
```
python 3.6 manage.py createsuperuser
```
and fill-in your credentials

* run the application using 
```
python3.6 manage.py runserver
```

* navigate to the admin panel by typing 
```
localhost:8000/admin
```

## Running the tests

Run the following commands:
```
python3.6 manage.py tests
```

## Deployment

View the following [document](https://github.com/jakhax/deploying-django-to-heroku-manual) inorder to deploy to a live system

## Built Using

* [Django](https://www.djangoproject.com/download/)
* [Bootstrap](https://getbootstrap.com)
* [MDBootstrap](https://mdbootstrap.com/)
* Html
* Python

## Contact Info

* Phone: +254722894999
* Email: marcusjnls@gmail.com
* Github Link: [Marcusjnls](https://github.com/Marcusjnls)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

