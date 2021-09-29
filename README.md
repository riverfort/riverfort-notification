# riverfort-notification

## Setup virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

## Install
```
cd riverfort-notification
pip install -r requirements.txt
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
```
cd riverfort-notification
python3 database/create_schema.py
python3 database/setup_companies.py
```

## Apply formatting
```
black .
```
---
## Company list
### LSE
  * Instrument list download: https://docs.londonstockexchange.com/sites/default/files/reports/Instrument%20list_14.xlsx
  * The file is updated monthly and published in the first week of the month. [Link](https://www.londonstockexchange.com/reports?tab=instruments)
  * Capture shares sheet only for news.
