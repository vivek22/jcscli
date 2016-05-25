import json

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
        ## json validation ##
	print "json is validated"
    except ValueError, e:
        return False
    return True

def get_vpc_id(vpcjson):
        data = json.loads(vpcjson)
        vpc_id = data['DescribeVpcsResponse']['vpcSet']['item']['vpcId']
	return vpc_id

def get_subnet_id(subnetjson):
        data = json.loads(subnetjson)
        subnet_id=data['DescribeSubnetsResponse']['subnetSet']['item']['subnetId']
	return subnet_id
    
def get_securitygroup_id(securitygroupjson):
        data = json.loads(securitygroupjson)
        securitygroup_id=data['DescribeSecurityGroupsResponse']['securityGroupInfo']['item'][2]['groupId']
	return securitygroup_id

def get_routetable_id(routetablejson):
        data = json.loads(routetablejson)
        routetable_id=data['CreateRouteTableResponse']['routeTable']['routeTableId']
        return routetable_id

def get_association_id(associatejson):
        data = json.loads(associatejson)
        association_id = data['AssociateRouteTableResponse']['associationId']
        return association_id

def get_allocation_id(addressesjson):
        data = json.loads(addressesjson)
        allocation_id=data['DescribeAddressesResponse']['addressesSet']['item']['allocationId']
        return allocation_id
