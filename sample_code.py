import requests
import json
from flask import Flask


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	data = {'get':get_request('http://131.227.90.10:3000/api/sensors?type=weight')}
	return '''
<html>
    <head>
        <title>Web Application and Web Services</title>
    </head>
    <body>
    	<h1> Sample get reqeust. Return the sensors whose type is weight</h1>
        <p> ''' + data['get'] + '''</p>
        <h1> Sample post request. Add a new sensor. </h1>
        <div> <a href='/add_sensor'>Add Sensor</a></div>
    </body>
</html>'''


@app.route('/add_sensor')
def add_sensor():
	data = {'post':post_request("{\n\t\"id\": \"54\",\n\t\"type\": \"Weight Scales\",\n    \"name\": \"Bathroom Scales\",\n\t\"subject\": \"3\"\n}")}
	return '''
<html>
    <head>
        <title>Web Application and Web Services</title>
    </head>
    <body>
        <h1> Add a new sensor. The sensor id is 54, type is Weight Scales, name is Bathroom Scales, subject id is 3</h1>
        <h1> It is supporsed to return an error since the sensor id is already exist.</h1>
        <p> ''' + data['post'] + '''</p>
    </body>
</html>'''




#This function is an example of requesting sensor information by type.
"""
	url - The url link to get the response from server. You can change it to list different sensors.
"""
def get_request(url):
	payload = {}
	headers = {}
	response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
	return response.text

#This function is an example of creating new sensors.
"""
	payload - the information of sensor which you send to the server.
"""
def post_request(payload):
	url = 'http://131.227.90.10:3000/api/sensors'
	headers = {
		'Content-Type': 'application/json'
	}
	response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
	return response.text
	


if __name__ == '__main__':
	app.run()
