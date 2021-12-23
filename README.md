# flask-shenanigans
Trying out Flask. Implemented a simple login system, which stores users on a RDS Postgres instance.

## Getting Started
If you want to run this application locally for yourself then you will need to do a couple of things. 
First thing you want to do is install all the dependencies. 
```
pip install -r requirements.txt
```

Secondly, you will need a Postgres database. Once you have that setup, create a `.env` file in the project's root directory with the following structure.
```
PSQL_HOST=<YOUR-DB-HOST>
PSQL_DBNAME=<YOUR-DBNAME>
PSQL_USER=<YOUR-DB-USER>
PSQL_PASSWORD=<YOUR-DB-PASSWORD>
```

Once you have that simply change directory into flaskr with `cd flaskr` and star the server with `flask run`.
