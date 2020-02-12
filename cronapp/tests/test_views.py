from django.test import TestCase
from cronapp.models import CronEgg
from uploadapp.models import File
from rest_framework.test import RequestsClient
from rest_framework.test import APITestCase
import json
# local server have to run

client = RequestsClient()


#def test_api_request():

url = 'http://localhost:8000/cron/'
response = client.get(url)
print(response.status_code)
assert response.status_code == 200


response3 = client.get(url + "1/")
print(response3.status_code)
assert response3.status_code == 200

response2 = client.post(url, data = json.dumps({"egg": 1, "cron_string": "******"}))
print(response2.text)
print(response2.status_code)
assert response2.status_code == 201

print(json.loads(response2.text)['cron_job_id'])

response5 = client.put(url + str(json.loads(response2.text)['cron_job_id'])+ "/", data = json.dumps({"cron_string":"11111"}))
print(response5.text)
print(response5.status_code)
assert response5.status_code == 201

response4 = client.delete(url + str(json.loads(response2.text)['cron_job_id'])+ "/")
print(response4.text)
print(response4.status_code)
assert response4.status_code == 201