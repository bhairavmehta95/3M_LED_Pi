import semsiot
import time 
import requests
import json

# Base URL as asssigned by SEMS
BASE_URL = "https://semsiot.3m.com/"


## TO DO: CONFIGURE DEVICE HERE

# DEVICE_ID = {{ Put Device ID Here }}

DEVICE_ID = '1'

def register_connect_device():
	headers = { 'Content-Type' : 'application/json' }
	
	# Query parameters to Connect
	## CONNECT IS THE SAME THING AS REGISTER
	register_url = BASE_URL + '/api/Register'
	query_parameters_register  = {
		"serialNumber" : "123456123456",
		"applicationId": "EBE05BA5-74A7-4152-9BF4-1EE5A9A64CDC",
		"apiKey": "gcT1vVuu=gwwspFsjkwg2hh2zFPDmmlWJanTSDq7pktnT",
		"deviceName": "led-indicator",
		"latitude" : 44.94,
		"longitude" : -93.09
	}
	
	# Posts a request with above parameters, we are looking for the two
	# Key values listed below
	
	response = requests.post(register_url , headers = headers, data = json.dumps(query_parameters_register) )	
	
	Authorization = response.json()['EventHubKey']
	event_hub_url = response.json()['EventHubUrl']

	# Authorizes connection
	headers.update( { 'Authorization' : Authorization } )
	#print headers
	return headers
	

# Sends post requests to update BT status
def send_bluetooth(bluetooth_status, headers):
	query_parameters_post = {
		"serialNumber" : "123456123456",
		"applicationId": "EBE05BA5-74A7-4152-9BF4-1EE5A9A64CDC",
		"apiKey": "gcT1vVuu=gwwspFsjkwg2hh2zFPDmmlWJanTSDq7pktnT",
		"bluetooth_status" : bluetooth_status,
		"deviceDataTypeCode" : "HEARTBEAT",
                "device_id" : DEVICE_ID,
	}
	
	# configures a URL for the data, posts same thing
	post_data_url = BASE_URL + '/api/Data'
	
	# Posts data (in this case status)
	response = requests.post(post_data_url, headers = headers, data = json.dumps(query_parameters_post))
	#print response

def get_status_text(headers):
	query_parameters_get = {
		"serialNumber" : "123456123456",
   		"applicationId": "EBE05BA5-74A7-4152-9BF4-1EE5A9A64CDC",
    	"apiKey": "gcT1vVuu=gwwspFsjkwg2hh2zFPDmmlWJanTSDq7pktnT",
	}

	get_url = BASE_URL + "/api/Data?request.applicationId=EBE05BA5-74A7-4152-9BF4-1EE5A9A64CDC%20&request.aPIKeyValue=InATu7b3CgBJsCUWfu%3D964d1fZdK1HKqgbs5K%3DetEYqzB&request.serialNumber=123456123456&request.lastXMinutes=120&request.historical=true"
	response = requests.get(get_url, headers = headers, data = json.dumps(query_parameters_get))
	#print "Here is the status code: ", response.status_code
	response_json = response.json()
	#print response_json
	# default
	status = 'Free'
	
	for entry in response_json['Data']:
		try:
                        if entry['device_id'] == DEVICE_ID:
                                if entry['status'] != '':
                                        status = entry['status']
		except:
			pass	
	
	#print "Returning: ", status
	return status
	
		
		

