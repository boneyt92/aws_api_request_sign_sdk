# AWS Version 4 api request signing Algorithm
# Technix Cloud SDK

from aws_sign_post import sign_request
import requests

#------------ Configuration Data--------------
method = 'POST'
service = 'execute-api'
host = ''
region = 'us-east-1'
endpoint = ''
content_type = 'application/json'
amz_target = ''

#------------ Confidential Data--------------

access_key = ''
secret_key = ''

#------------ URL Data -------------------------

canonical_uri = ''
canonical_querystring = '' # Leave Blank for POST Method
request_parameters =   ''  # Data to be sent in json format.

# ************* Generate the Signature and Headder *************
headers = sign_request(method,service,host,region,content_type,amz_target,access_key,secret_key,canonical_uri,canonical_querystring,request_parameters)

# ************* SEND THE REQUEST *************
print '\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++'
print 'Request URL = ' + endpoint

r = requests.post(endpoint, data=request_parameters, headers=headers)

print '\nRESPONSE++++++++++++++++++++++++++++++++++++'
print 'Response code: %d\n' % r.status_code
print r.text
