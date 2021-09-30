# riverfort-notification
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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
python3 database/setup_exchanges.py
python3 database/setup_companies.py
```

## Apply formatting
```
black .
```
---
## Company list
### London
  * Instrument list download: https://docs.londonstockexchange.com/sites/default/files/reports/Instrument%20list_14.xlsx
  * The file is updated monthly and published in the first week of the month. [Link](https://www.londonstockexchange.com/reports?tab=instruments)
  * Capture shares sheet only for news.
### AQS
  * Instrument list download: https://aquis-website-eu.s3.amazonaws.com/primary_aqse_summary_july_21.xls
  * The file seems updated monthly. [Link](https://www.aquis.eu/aquis-stock-exchange/for-investors/market-statistics-data)
  * Capture All AQSE securities.
