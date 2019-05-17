# Lambda methond: http-responder tester

import requests

# hooks into ApiGW:'API for Responder' on the back end
address = 'https://l3vwpri01a.execute-api.us-east-1.amazonaws.com/BetaStage'
response = requests.get(address)

print(response)
print (type(response))
print (response.json)
print (response.headers)
print (response.headers['date'])
print (response.text)