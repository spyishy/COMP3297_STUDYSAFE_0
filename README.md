# StudySafe (Core + Trace)

---

## Local setup

Create virtual environment and install dependencies:

```
pipenv --three
pipenv install
pipenv shell
```

Run server locally:

```
python manage.py runserver
```

---

## Heroku product

Django Admin:

```
https://studysafe-b-group-e.herokuapp.com/admin/
```

StudySafe Core APIs:

```
https://studysafe-b-group-e.herokuapp.com/api/
```

StudySafe Trace Web Display:

```
https://studysafe-b-group-e.herokuapp.com/trace/venues/<hku_id>/<date>/
```
