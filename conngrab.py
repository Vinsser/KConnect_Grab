import requests
import argparse
import json
import warnings

warnings.filterwarnings("ignore")

## Setting up parser
parser = argparse.ArgumentParser()
parser.add_argument('connector_url', type=str, help='url for connector instance')
parser.add_argument('-a', '--all_status', action='store_true', help='To get status for all connectors')
parser.add_argument('-A', '--all_config', action='store_true', help='To get config for all connectors, params is required')
parser.add_argument('-c', '--conn', type=str, metavar='', help='To get status for a specific connector')
parser.add_argument('-C', '--config', type=str, metavar='', help='To get config for a specific connector')
parser.add_argument('-p', '--param', type=str, metavar='', help='specify a parameter from a config')
args = parser.parse_args()

seed_url = args.connector_url

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# get config
def get_config(conn):
    config_url = seed_url + '/' + conn + '/config'
    config_response = requests.get(config_url, verify=False)
    if (args.param): return args.param + ': ' + config_response.json()[args.param]
    else: return config_response.json()

# get multiple config
def get_configs():
    for conn in connectors:
        if (args.param): 
            print(conn)
            print(get_config(conn))
        else: print("please specify params")
        print('\n')

# method to get status
def get_status(conn):
    status_url = seed_url + '/' + conn + '/status'
    status_response = requests.get(status_url, verify=False)
    return status_response.json()

# method to display a single available connector status
def one_displ(conn):
    status_dict = get_status(conn)
    print('connector_name: ' + status_dict['name'], '|','connector_state: ' + status_dict['connector']['state'])
    jprint(status_dict['tasks'])
    #if status_dict['state'] == 'FAILED': print(seed_url + '/' + conn + '/tasks/' + str(status_dict['id']) + '/restart')

# method to display all available connector status
def all_displ():
    for conn in connectors:
        status_dict = get_status(conn)
        print('##############################')
        print('connector_name: ' + status_dict['name'], '|','connector_state: ' + status_dict['connector']['state'])
        for T in status_dict['tasks']:
            print( T['id'], T['state'])
            if T['state'] != 'RUNNING': print(seed_url + '/' + conn + '/tasks/' + str(T['id']) + '/restart')
        print('\n')

if __name__ == '__main__':

    seed_response = requests.get(seed_url, verify=False)
    connectors = seed_response.json()

    if (args.all_status): all_displ()
    elif (args.all_config): get_configs()
    elif (args.conn): one_displ(args.conn)
    elif (args.config): jprint(get_config(args.config))
    else: jprint(connectors)





