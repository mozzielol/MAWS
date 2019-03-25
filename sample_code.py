import requests
import json

def get_request(url):
	payload = {}
	headers = {}
	response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
	print(json.dumps(response.json(),indent=2))


def post_request():
	url = 'http://131.227.90.10:3000/api/sensors'
	#payload = "{\n\t\"id\": {1},\n\t\"type\": {2},\n    \"name\": {3},\n\t\"subject\": {4}\n}".format(id,type,name,subject)
	payload = "{\n\t\"id\": \"54\",\n\t\"type\": \"Weight Scales\",\n    \"name\": \"Bathroom Scales\",\n\t\"subject\": \"3\"\n}"
	headers = {
		'Content-Type': 'application/json'
	}
	response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
	print(json.dumps(response.json(),indent=2))


if __name__ == '__main__':
	get_urls = {
	'Get the sensor by Type': 'http://131.227.90.10:3000/api/sensors?type=weight',


	}
	for request_name, url in get_urls.items():
		print(request_name,end=' : ')
		get_request(url)
		print('--'*20)

	post_request()