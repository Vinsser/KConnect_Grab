import requests
import json
import sys

args = sys.argv[1:]
seed_url = str(args[0])

if (len(args) < 2) : step_arg = 'default' 
else: step_arg = args[1]

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# method to grab a single available connector config
def one_status(conn):
    status_url = seed_url + '/' + conn + '/status'
    status_response = requests.get(status_url, verify=False)
    status_dict = status_response.json()
    print('connector_name: ' + status_dict['name'], '|','connector_state: ' + status_dict['connector']['state'])
    jprint(status_dict['tasks'])
    #if status_dict['state'] == 'FAILED': print(seed_url + '/' + conn + '/tasks/' + str(status_dict['id']) + '/restart')

# method to grab all available connector configs
def all_status():
    for conn in connectors:
        status_url = seed_url + '/' + conn + '/status'
        status_response = requests.get(status_url, verify=False)
        status_dict = status_response.json()
        #jprint(status_reponse.json())
        print('##############################')
        print('connector_name: ' + status_dict['name'], '|','connector_state: ' + status_dict['connector']['state'])
        for T in status_dict['tasks']:
            print( T['id'], T['state'])
            if T['state'] == 'FAILED': print(seed_url + '/' + conn + '/tasks/' + str(T['id']) + '/restart')
            if T['state'] == 'UNASSIGNED': print(seed_url + '/' + conn + '/tasks/' + str(T['id']) + '/restart')
        #print( [(T['id'], T['state']) for T in status_dict['tasks']] )
        print('\n')
        #print(status_dict)

seed_response = requests.get(seed_url, verify=False)
connectors = seed_response.json()

if step_arg == 'default': jprint(connectors) 
elif step_arg == 'all': all_status()
else: one_status(step_arg)
    




