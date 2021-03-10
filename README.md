

# Base Django Project

## Introduction

Base Project is an application written in Python using Django Framework and PostgreSQL as the database.


## Requirements

- Python >= 3.8
- PostgreSQL 12.0

## Traditional Setup

If you want to use docker, [skip](#docker-setup) to the subsequent section for instrunctions.


### PostgreSQL

Ensure you have a PostgreSQL server runing on your machine and create a database with `psql`:

```bash
$ psql -h 127.0.0.1 -U <your_username> -W

# create your database
$ CREATE DATABASE <your_database>;
$ \q
```

### Environment Variables

Then, set the following environment variables (you can create a file named `.env` in the project root):

```env
DJANGO_DEBUG=1
DB_HOST=127.0.0.1
DB_NAME=<your_username>
DB_USER=<your_database>
DB_PASSWORD=<db_password>
DB_PORT=5432
```

### Python Environment

You should install `pipenv` to manage your project environment:

```sh
$ pip install -U pip
$ pip install pipenv
$ pipenv sync --dev
```

Enable virtualenv with pipenv:

```sh
$ pipenv shell
```

Apply migrations into database:

```sh
$ python manage.py migrate
```

Create a new user to access the admin site:

```sh
$ python manage.py createsuperuser
```

And then, start the server:

```sh
$ python manage.py runserver 0.0.0.0:8000
```

## <a name="docker-setup"></a>Docker Setup

### Requirements

- Docker
- docker-compose

Into the project root, type:

```sh
$ docker-compose up -d
```

Apply migrations:

```sh
$ docker-compose run --rm web migrate
```

To create an admin user:

```sh
$ docker-compose run --rm web createsuperuser
```

To stop the service, type:

```sh
$ docker-compose down
```
