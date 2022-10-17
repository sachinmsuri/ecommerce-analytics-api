eCommerce Analytics API
===

## Overview

Flask REST API developed using Flask Rest-X to allow users to fetch a variety of analytics details from an eCommerce store.
When running the the Flask App, swagger documentation for the API can be viewed at localhost.


## Installation

Install requriments for project into virtual environment
```bash
pip install -r requirements.txt
```

Set api/ as FLASK_APP location
```bash
export FLASK_APP=api/
```

Create SECRET_KEY and add to .env file
```python
import secrets

secrets.token_hex()
```

Run flask shell and create database
```bash
flask shell

db.create_all()
```

Run flask shell and create database
```bash
flask shell

db.create_all()
```

Run Flask Application
```bash
python app.py
```

Add data to database
```bash
python api/upload_data.py
```







