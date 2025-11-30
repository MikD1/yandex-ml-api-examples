import requests

method = "GET"
url = "http://jsonplaceholder.typicode.com/posts/42"
headers = {
    "Accept": "application/json"
}
body = None

response = requests.request(method, url, headers=headers, data=body)

print("Status:", response.status_code)
print("Response")
print(response.text)
