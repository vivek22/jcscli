import json

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
        ## json validation ##
	print "json is validated"
    except ValueError, e:
        return False
    return True

def get_accesskey_value(accesskeyjson):
        data = json.loads(accesskeyjson)
        accesskey_value=data['credentials'][0]['blob']['access']
	return accesskey_value


