import requests as request

response = request.get('https://stackoverflow.com/asdasd')
print(response.status_code)