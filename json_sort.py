import json
from pprint import pprint

def ordered(obj):
		if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


with open('derp.json') as data_file:    
    data = json.load(data_file)
		
#sorted_obj = dict(data) 

##pprint(sorted_obj)

#sorted_obj = sorted(sorted_obj, key=sorted_obj.get)
#only works on top level json objects(not for arrays)
sorted(data)
#compare two sorted jsons
#sorted(a.items()) == sorted(b.items())
#pprint(sorted_obj)


ordered(a) == ordered(b)


with open('sorted_stuff.json', 'w') as f:
     #json.dump(sorted_obj, f, sort_keys=True )
		 json.dump(data, f)