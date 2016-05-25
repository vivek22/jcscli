import json

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
        ## json validation ##
	print "json is validated"
    except ValueError, e:
        return False
    return True

def get_image_id(imagejson):
        data = json.loads(imagejson)
        image_id=data['DescribeImagesResponse']['imagesSet']['item'][3]['imageId']
	return image_id

def get_instancetype_id(instancetypejson):
        data = json.loads(instancetypejson)
        instancetype_id=data['DescribeInstanceTypesResponse']['instanceTypes']['item'][2]['id']
	return instancetype_id
    
def get_keypair_id(keypairjson):
        data = json.loads(keypairjson)
        keypair_id=data['DescribeKeyPairsResponse']['keySet']['item'][0]['keyName']
	return keyname_id

def get_volume_id(volumejson):
        data = json.loads(volumejson)
        volume_id=data['DescribeVolumesResponse']['volumeSet']['item'][0]['volumeId']
        return volume_id

def get_sbsvolume_id(sbsvolumejson):
        data = json.loads(sbsvolumejson)
        sbsvolume_id=data['"CreateVolumeResponse"']['volumeId']
        return sbsvolume_id

def get_snapshot_id(snapshotjson):
        data = json.loads(snapshotjson)
        snapshot_id=data['DescribeSnapshotsResponse']['snapshotSet']['item']['snapshotId']
        return snapshot_id

def get_instance_id(instancejson):
        data = json.loads(instancejson)
        instance_id=data['DescribeInstancesResponse']['instancesSet']['item']['instanceId']
        return instance_id

def get_routetableforroute_id(routetablejson):
        data = json.loads(routetablejson)
        routetable_id=data['DescribeRouteTablesResponse']['routeTableSet']['item']['routeTableId']
        return routetable_id

