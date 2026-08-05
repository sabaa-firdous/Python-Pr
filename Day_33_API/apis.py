import requests

response= requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data=response.json()['iss_position']
print(data)
# print(response)
# print(response.status_code)
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")
# elif response.status_code==401:
#     raise Exception("You are not allowed to this data")
# elif response.status_code==401:
#     raise Exception("This resource does not exist")