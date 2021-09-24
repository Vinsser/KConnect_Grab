# KConnect_Grab
Python tool to grab configs/status for Kafka Connectors

#### Usage
python -Wignore conngrab.py https://abc.xyz.com/connectors - displays connectors list

$python -Wignore conngrab.py -h
usage: conngrab.py [-h] [-a] [-c] connector_url

positional arguments:
  connector_url     url for connector instance

optional arguments:
  -h, --help        show this help message and exit
  -a, --all_status  To get status for all connectors
  -c , --conn       To get status for a specific connector
