import sys
import json
import pydash
from urllib.request import urlopen, Request

def get_json_dict_from_url(url):

    r = Request(url,headers={"Accept":"application/json"})

    with urlopen(r) as response:
        #print(response.status)
        #print(response.read().decode())
        text = response.read().decode()
        return json.loads(text)

#recursively resolve json file data.
def resolve_extended_json_file(file_data_dict):
    #print(file_data_dict)

    if 'extends' not in file_data_dict.keys():
        #print("Got here.")
        #print(file_data_dict)
        return file_data_dict
    
    #fetch the dict that is in the 'extends' tag
    superJsonDict = get_json_dict_from_url(file_data_dict['extends'])

    del file_data_dict['extends']

    resolve = resolve_extended_json_file(superJsonDict)

    pydash.merge(resolve, file_data_dict)

    resolve['rules'].update(file_data_dict)
    resolve['rules'].pop('axioms')
    resolve['rules'].pop('$schema')
    resolve['rules'].pop('version')
    resolve['rules'].pop('rules')

    return resolve

#Grab base url 
baseUrl = sys.argv[1]

print(json.dumps(resolve_extended_json_file(get_json_dict_from_url(baseUrl))))