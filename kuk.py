import requests
r = requests.get(https://www.youtube.com)
print(type(r))
print(r.status_code)