# Hexagonal Architecture example in Python using FastAPI and SQLAlchemy

## Installation and Usage

With docker installed, run the following:

```
    $ git clone git@github.com:S0Smislom/hexagonal-architecture-fastapi.git
    $ cd hexagonal-architecture-fastapi
    $ docker network create example-net
    $ docker compose up
```

To run migrations:
```
    $ docker exec -it example-api /bin/bash
    $ cd adapters/repository/sqlalchemy
    $ alembic upgrade head
```
