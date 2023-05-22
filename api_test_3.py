import requests

response = requests.get('https://playground.learnqa.ru/api/hello')

print('GET https://playground.learnqa.ru/api/hello')
print(f'\nResponse text: \n{response.text}')
print('-----')
print(f'Status code: \n{response.status_code}')
print('-----')
print(f'Headers: \n{response.headers}')
print('-----')
print(f'Is Redirect: \n{response.is_redirect}')
print('-----')
print(f'Response URL: \n{response.url}')
