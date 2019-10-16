# Insta_Gram

This is an attempt at cloning the social media site instagram where users share comment and like photos

## Author

* **Marcus Jean-Louis** - *Initial work* - [Marcusjnls](https://github.com/Marcusjnls)

# Application Screenshots

![personprofile](screenshots/personprofile.png)

![homepage](screenshots/Home.png)

![likesandcomments](screenshots/likes.png)

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

1. set up a virtual environment using the following command

```
python3.6 -m venv --without-pip virtual
```

And activate it

```
source virtual/bin/activate
```
1. install the latest version of pip

```
curl https://bootstrap.pypa.io/get-pip.py | python
```

1. Install the requirements in the requirements.txt file using
```
pip install -r requirements.txt
```
1. create a .env file in your rootfolder and add the following configurations
```
SECRET_KEY='<random-string>'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='postgres://databaseowner:password@localhost/databasename'
```
1. create postgres database
```
CREATE DATABASE <your-database-name>
```
1. create a migration using the following command
```
python3.6 manage.py makemigrations
```

and migrate

```
python3.6 manage.py migrate
```
1. create an admin account
```
python 3.6 manage.py createsuperuser
```
and fill-in your credentials

1. run the application using 
```
python3.6 manage.py runserver
```
1. navigate to the admin panel by typing 
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

