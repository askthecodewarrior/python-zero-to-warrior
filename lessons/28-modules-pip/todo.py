# A package from PyPI
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)
print(response.json())
