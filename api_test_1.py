import requests

# expected response: {"answer":"Hello, someone"}
response_1 = requests.get('https://playground.learnqa.ru/api/hello')

print('GET https://playground.learnqa.ru/api/hello')
print(response_1.text)

# expected response: {"answer":"Hello, alex"}
response_2 = requests.get('https://playground.learnqa.ru/api/hello?name=alex')

print('GET https://playground.learnqa.ru/api/hello?name=alex')
print(response_2.text)
