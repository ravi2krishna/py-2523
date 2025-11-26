# External Modules
# import requests # ModuleNotFoundError: No module named 'requests'
# install using -> pip install requests
import requests
response = requests.get('https://www.python.org/')
print(response.status_code)

response = requests.get('https://www.python.org/ravi')
print(response.status_code)

if response.status_code != 200:
    print("Resource Not Found")
else:
    print("Resource Found")
