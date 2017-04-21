import requests

client_id = '8f3bf8863eaacba15f39'
client_secret = 'a959d4a132a18c99946fb69b9fec12633006958e'
code = '20bc189a0987774dba3b'
access_token = 'ee0a5f24e9ca43cc0ca314f069a8ca163490532d'

if __name__ == '__main__':
	url = 'https://api.github.com/user/repos'
	headers = {'Authorization': 'token ee0a5f24e9ca43cc0ca314f069a8ca163490532d'} 	#requiere  authentication

	response = requests.get(url, headers= headers)	#obtenemos esa respuesta
	if response.status_code == 200:
		response_json = response.json()		#se le pasan todos los endpoits a response_json
		for projects in response_json:		#iteramos a response y objenemos la key de name de los projectos
			name = projects['name']
			print(name)

	else:
		print(response.content)
	
