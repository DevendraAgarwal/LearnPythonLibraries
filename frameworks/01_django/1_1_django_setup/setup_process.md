# Django Setup Process

## Environment Setup

```shell
# install pip
python -m pip install -U pip

# create Environment
python -m venv env_site
source env_site/bin/activate

# install dependencies
pip install django

```

## Django Installation

With Django installed, you can create a new project using the _django-admin_ command. Replace <project_name> with your desired project name:

```shell
# start new project
django-admin startproject <project_name>

# start the server
cd geeks_site
python manage.py runserver

# verify server status by visiting http://127.0.0.1:8000/

```

## Directory Structure

<project_name>/: The project directory.

**manage.py**: A command-line utility for interacting with the project.
**<project_name>/settings.py**: Configuration settings for the project.
**<project_name>/urls.py**: URL declarations for the project.
**<project_name>/wsgi.py**: Entry-point for WSGI-compatible web servers.
**<project_name>/asgi.py**: Entry-point for ASGI-compatible web servers.

## Create Django App

A Django project can contain multiple apps. To create an app, use the startapp command. Replace <app_name> with your desired app name:

```shell
python manage.py startapp <app_name>
```

## App Directory Structure

This command creates a directory structure for the app, which includes:

<app_name>/: The app directory.

**models.py**: Define the data models.
**views.py**: Define the views.
**urls.py**: Define the URL patterns.
**admin.py**: Register models with the admin site.
**apps.py**: App configuration.
**migrations/**: Database migrations.

Your Project Folder Structure will look like this.

```
project_name/
│
├── app_name/
│   │
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── project_name/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```
