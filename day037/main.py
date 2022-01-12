import requests
import datetime as dt

# GET, POST, PUT, DELETE

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_NAME = "********"
TOKEN = "********"
# Call /v1/users API by HTTP POST.
pixela_params ={
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(PIXELA_ENDPOINT, json=pixela_params)
# print(response.text)

GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USER_NAME}/graphs'
GRAPH_ID = "graph1"

graph_params = {
    "id": "graph1",
    "name": "Coding graph",
    "unit": "Minutes",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url = GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}'

# today = str(dt.datetime.now().date()).replace("-", "")
today = dt.datetime.now()
# print(today.strftime("%Y%m%d"))

one_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "120"
}

response = requests.post(url=PIXEL_ENDPOINT, json=one_pixel_params, headers=headers)
print(response.text)

# PUT - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
day_to_edit = "20220111"
PUT_ENDPOINT = f'{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{day_to_edit}'
put_pixel_params = {
    "quantity": "180"
}
# response = requests.put(url=PUT_ENDPOINT, json=put_pixel_params, headers=headers)
# print(response.text)

# DELETE - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
day_to_delete = "20220110"
DELETE_ENDPOINT = f'{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{day_to_delete}'

response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
print(response.text)