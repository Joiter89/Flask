import requests

response = requests.post('http://127.0.0.1:5000/ad/',
                         json={'header': 'header',
                               'description': 'Hi guys',
                               'owner': 'Svetlana'}

                         )
print(response.status_code)
print(response.json())

response = requests.get('http://127.0.0.1:5000/ad/1')
print(response.status_code)
print(response.json())

response = requests.delete(
    "http://127.0.0.1:5000/ad/1",
)
print(response.status_code)
print(response.json())