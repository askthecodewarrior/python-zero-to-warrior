# A package from PyPI: print only the title
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)
print(response.json()["title"])
