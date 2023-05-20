import requests

response_1 = requests.get('https://playground.learnqa.ru/api/get_text')

print('GET https://playground.learnqa.ru/api/get_text')
print(response_1.text)

response_2 = requests.get('https://playground.learnqa.ru/api/get_text?name=alex')

print('GET https://playground.learnqa.ru/api/get_text?name=alex')
print(response_2.text)
