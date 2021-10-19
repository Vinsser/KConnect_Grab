# KConnect_Grab
Python tool to grab configs/status for Kafka Connectors

#### Usage
python conngrab.py https://abc.xyz.com/connectors - displays connectors list

$python conngrab.py -h
usage: conngrab.py [-h] [-a] [-A] [-c] [-C] [-p] connector_url

positional arguments:
  connector_url     url for connector instance

optional arguments:\
  -h, --help        show this help message and exit\
  -a, --all_status  To get status for all connectors\
  -A, --all_config  To get config for all connectors, params is required\
  -c , --conn       To get status for a specific connector\
  -C , --config     To get config for a specific connector\
  -p , --param      specify a parameter from a config\
  -R, --restart_all  restart all failed tasks