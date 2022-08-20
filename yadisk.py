import requests

token = input('Введите токен:\n')
filename = input('Введите полное имя файла:\n')

def get_upload_url():
	url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
	upload_url = requests.get(url, headers={'Content-Type': 'application/json',
	                                        'Authorization': f'OAuth {token}'},
	                          params={'overwrite': 'true', 'path': f'{filename}'})
	return upload_url.json()


requests.put(get_upload_url().get('href', ''), data=open(f'{filename}', 'rb'))
