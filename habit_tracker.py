import requests
from datetime import datetime

USERNAME = ''
TOKEN = ''
GRAPH_ID = "graph1"
pixela_endpoint = 'https://pixe.la/v1/users'
today = datetime.today()
print(today)

params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    'X-USER-TOKEN':TOKEN
}

# graph_config = {
#     "id":"graph1",
#     "name":"Jogging Graph",
#     "unit":"Km",
#     "type":"float",
#     "color":"shibafu",
# }

# requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date":today.strftime('%Y%m%d'),
    "quantity": input("How many Km did you run today? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)
