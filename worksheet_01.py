import requests
import json

seed_url = 'https://hybrid-data-delivery-kafka-connect-gcp-dev.bigdatainfrastructure.k8s.genmills.com/connectors/SupplyChain_ER_Partition_Shrink/status'

seed_response = requests.get(seed_url, verify=False)

#print(type(seed_response.json()))
seed_dict = seed_response.json()

#print(seed_json['name'])
print('name: ' + seed_dict['name'], '|','connector_state: ' + seed_dict['connector']['state'])
for T in seed_dict['tasks']:
    print( T['id'], T['state'] )
#print([T['id'] for T in seed_dict['tasks']])