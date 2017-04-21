import requests

client_id = '8f3bf8863eaacba15f39'
client_secret = 'a959d4a132a18c99946fb69b9fec12633006958e'
code = '20bc189a0987774dba3b'
access_token = 'ee0a5f24e9ca43cc0ca314f069a8ca163490532d'
#https://github.com/login/oauth/authorize?client_id=8f3bf8863eaacba15f39&scope=respo  con esto tengo code
if __name__ == '__main__':
	url = 'https://github.com/login/oauth/access_token'
	payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}	#documentacion en github step 1
	headers = {'Accept':'application/json'}		#documentacion step 2

	response = requests.post(url, json=payload, headers = headers)	#post
	if response.status_code == 200:
		response_json = response.json()
		access_token = response_json['access_token']	#obtener access token del oauth
		print(access_token)
