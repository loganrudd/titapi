import requests
import json

# define URL and file_path to data
url = 'http://127.0.0.1:8000/passengers'

payload = json.dumps({
	"pclass": 3,
	"sex": 0,
	"age": 2,
	"fare": 0,
	"embarked": 2,
	"title": 1,
	"is_alone": 1,
	"age_class": 6
})

headers = {'Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
