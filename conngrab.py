import requests
import json

seed_url = 'https://hybrid-data-delivery-kafka-connect-gcp-dev.bigdatainfrastructure.k8s.genmills.com/connectors'
#seed_url = 'https://hybrid-data-delivery-kafka-connect-gcp-qa.bigdatainfrastructure.k8s.genmills.com/connectors'
#seed_url = 'https://hybrid-data-delivery-kafka-connect-gcp-prod.bigdatainfrastructure.k8s.genmills.com/connectors'

#connectors = []

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

seed_response = requests.get(seed_url, verify=False)

connectors = seed_response.json()

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
    #print( [(T['id'], T['state']) for T in status_dict['tasks']] )
    print('\n')
    #print(status_dict)


