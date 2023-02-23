> tool to create flask websites

# Topics

- [Topics](#topics)
  - [Project workflow](#project-workflow)
- [Requirements](#requirements)
- [How to use](#how-to-use)

### Project workflow

```
_backend
  └── public
  └── database
  └── src
  └── server.py

```

# Requirements

> :snake: Python 3x

> Flask, MySQLdb, uvicorn

> Git

# How to use

```sh
# Clone
$ git clone https://github.com/silascastro/productAPi.git
# Enter in the folder:
$ cd backend
# create a enviroment with
$ python3 -m venv venv
# activate the enviroment with
$ . venv/bin/activate
# Install the packages and libraries
$ pip install -r requirements.txt
# Run
$ uvicorn server:app --reload
```
# Update database to your local database on database script
```
  _backend
  └── src
   └── infra
    └── sqlalchemy
      └── config
        └── database.py 
```

```python   
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://<user>:<password>@127.0.0.1:3306/<database>"
```
