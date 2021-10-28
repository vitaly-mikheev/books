# BOOKS API with DRF

### Requirements

* virtualenv or virtualenvwrapper
* python3

### Running on local

Activate environment with virtualenv
```
[books] virtualenv -p python3 books_env
```
```
[books] . env/bin/activate
```

Activate environment with virtualenvwrapper

```
[books] mkvirtualenv books_env
```
```
[books] workon books_env
```

Install requirements

```
(books_env)[books] pip install -r requirements.txt
```

Migrate and runserver

```
(books_env)[books] python manage.py mirate
```
```
(books_env)[books] python manage.py runserver
```

### Create Superuser

```
(books_env)[books] python manage.py createsuperuser
```

### Endpoint and Admin

```
localhost:8000/admin/
```

```
localhost:8000/api/books/
```
