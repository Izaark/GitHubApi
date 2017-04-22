import requests

if __name__ == '__main__':
	url = 'http://api.github.com/user'

	session = requests.session()
	session.auth = ('purebas12322@gmail.com','pruebas123')

	response = session.get(url)
	if response.ok:
		response = session.get('https://github.com/pruebasapi')
		if response.ok:
			print(response.cookies)