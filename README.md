# riverfort-notification

## Setup virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

## Setup database [container](https://github.com/bitnami/bitnami-docker-postgresql)
```
docker run -d --name riverfort_notification \
-e POSTGRESQL_POSTGRES_PASSWORD=password123 \
-e POSTGRESQL_DATABASE=riverfort_notification \
-e POSTGRESQL_USERNAME=riverfort \
-e POSTGRESQL_PASSWORD=rgctechnology \
-p 5432:5432 \
bitnami/postgresql:11.4.0
```
```
psql -U riverfort -h localhost riverfort_notification
```
