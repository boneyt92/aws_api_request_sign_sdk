# AWS Version 4 signing
# Author: technixweb@gmail.com

import requests
import aws_api_sign_get


#-------------Configuration Data --------------
method = 'GET'
service = 'execute-api'
host = ''
region = ''
endpoint = ''
access_key = ''
secret_key = ''
canonical_uri = ''
#----------------------------------------------------------

request_parameters = ''  # Data to be sent


headers = aws_api_sign_get.sign_request(method, host, service, region,access_key,secret_key, canonical_uri, request_parameters)
canonical_querystring = request_parameters
request_url = endpoint + '?' + canonical_querystring

print '\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++'
print 'Request URL = ' + request_url
r = requests.get(request_url, headers=headers)

print '\nRESPONSE++++++++++++++++++++++++++++++++++++'
print 'Response code: %d\n' % r.status_code
print r.text

