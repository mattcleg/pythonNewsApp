import requests

auth_params = {'consumer_key': '72874-35e025a56922cbdf7a464256', 'redirect_uri': 'newsApp:authorizationFinished'}

tkn = requests.post('https://getpocket.com/v3/oauth/request', data=auth_params)

usr_params = {
    'consumer_key': '72874-35e025a56922cbdf7a464256',
    'code': 'ea55af37-40ed-d479-7e55-7f21be'
}

usr = requests.post('https://getpocket.com/v3/oauth/authorize', data=usr_params)
print(usr.content)