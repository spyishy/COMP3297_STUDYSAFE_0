# StudySafe (Core + Trace)

---

### Environment

Create virtual environment and install dependencies:

```
pipenv --three
pipenv install
```

---

### Run

Run server locally:

```
python manage.py runserver
```

---

### URLs (local server)

Django Admin:

```
127.0.0.1:8000/admin/
```

StudySafe Core APIs:

```
127.0.0.1:8000/api/venues/
127.0.0.1:8000/api/venues/<venue_code>/
127.0.0.1:8000/api/hku-members/
127.0.0.1:8000/api/hku-members/<hku_id>/
127.0.0.1:8000/api/entries/
127.0.0.1:8000/api/exits/
```

StudySafe Trace web display:

```
127.0.0.1:8000/trace/venues/<hku_id>/<date>/
127.0.0.1:8000/trace/contacts/<hku_id>/<date>/
```

---

### API documentation / examples for manual tests (e.g. using HTTPie)

Create Venue records:

```
http POST 127.0.0.1:8000/api/venues/ venue_code="CPD-LG.01" location="Centennial" type="LT" capacity="170"
http POST 127.0.0.1:8000/api/venues/ venue_code="CPD-LG.02" location="Centennial" type="CR" capacity="45"
http POST 127.0.0.1:8000/api/venues/ venue_code="CPD-LG.03" location="Centennial" type="TR" capacity="30"
http POST 127.0.0.1:8000/api/venues/ venue_code="CPD-LG.04" location="Centennial" type="LT" capacity="120"
```

Retrieve all or specific Venue records (specify HKU ID):

```
http GET 127.0.0.1:8000/api/venues/
http GET 127.0.0.1:8000/api/venues/CPD-LG.01/
```

Create HKU Member records:

```
http POST 127.0.0.1:8000/api/hku-members/ hku_id="3030000001" name="A"
http POST 127.0.0.1:8000/api/hku-members/ hku_id="3030000002" name="B"
http POST 127.0.0.1:8000/api/hku-members/ hku_id="3030000003" name="C"
http POST 127.0.0.1:8000/api/hku-members/ hku_id="3030000004" name="D"
```

Retrieve all or specific HKU Member records (specify HKU ID):

```
http GET 127.0.0.1:8000/api/hku-members/
http GET 127.0.0.1:8000/api/hku-members/3030000001/
```
