import requests

client_id = '8f3bf8863eaacba15f39'
client_secret = 'a959d4a132a18c99946fb69b9fec12633006958e'
code = 'bfbbb5ab644416bc80be'
access_token = 'af4bc9a0c053a89d74b0ed49898f7aa7d8c151df'

if __name__ == '__main__':
	url = 'https://api.github.com/user/repos'
	headers = {'Authorization': 'token ' + access_token} 	#requiere  authentication

	response = requests.get(url, headers= headers)	#obtenemos esa respuesta
	if response.status_code == 200:
		response_json = response.json()		#se le pasan todos los endpoits a response_json
		for projects in response_json:		#iteramos a response y objenemos la key de name de los projectos
			name = projects['name']
			print(name)

	else:
		print(response.content)
	
