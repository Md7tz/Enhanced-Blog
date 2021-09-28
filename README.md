> Enhanced Blog Django starter project.

## 🚀 Features

- Django 3.1 & Python 3.8
- Install via [Pip](https://pypi.org/project/pip/), [Pipenv](https://pypi.org/project/pipenv/)
- Static files configured with [Whitenoise](http://whitenoise.evans.io/en/stable/index.html)
- Styling with [Bootstrap v4](https://github.com/twbs/bootstrap)
- Forms with [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)

![Homepage](homepage.png)
----

## Table of Contents
* **[Installation](#installation)**
  * [Pip](#pip)
  * [Pipenv](#pipenv)
* [Setup](#setup)
* [Support](#support)
* [License](#license)

----

## 📖 Installation
DjangoX can be installed via Pip or Pipenv depending upon your setup. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/Md7tz/Enhanced-Blog.git
$ cd Enhanced-Blog
```

### Pip

```
$ python3 -m venv Enhanced-Blog
$ source Enhanced-Blog/bin/activate
(Enhanced-Blog) $ pip install -r requirements.txt
(Enhanced-Blog) $ python manage.py migrate
(Enhanced-Blog) $ python manage.py createsuperuser
(Enhanced-Blog) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

### Pipenv

```
$ pipenv install
$ pipenv shell
(Enhanced-Blog) $ python manage.py migrate
(Enhanced-Blog) $ python manage.py createsuperuser
(Enhanced-Blog) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

## Setup

```
# Run Migrations
(Enhanced-Blog) $ python manage.py migrate

# Create a Superuser
(Enhanced-Blog) $ python manage.py createsuperuser

# Confirm everything is working:
(Enhanced-Blog) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000
```

----

## ⭐️ Support

Give a ⭐️  if this project helped you!

## License

[The MIT License](LICENSE)
