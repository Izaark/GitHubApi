import requests

#https://github.com/login/oauth/authorize?client_id=8f3bf8863eaacba15f39&scope=repo
if __name__ == '__main__':

	client_secret = 'a959d4a132a18c99946fb69b9fec12633006958e'
	code = 'a8cc98e5c7cae38c3792'
	cliend_id = '8f3bf8863eaacba15f39'
	access_token = '0c6c85e7c3fe80a96422fd369692eebbb5fd69c8'

	url = 'https://api.github.com/user/repos'
	payload = { 'name' : 'testapi', 'description':'Testing commit 1', 'auto_init': True}
	headers = { 'Accept':'application/json', 'Authorization': 'token '+ access_token}
	print(payload)

	response = requests.post(url, json=payload ,headers=headers)


	if response.status_code == 200:
		print(response.json())
	else:
		print("Error",response.content)


