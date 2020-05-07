import http.client as client

'''this is a simple script, which can help you to check if your site works properly at the moment'''

print('paste your url, using www.(your site here).com')
url = input()

def getStatus():
    connection = client.HTTPSConnection(url)
    connection.request('GET', '/')
    response = connection.getresponse()
    if (response.status <300):
        print('connected propery without any redirects')
    elif (response.status < 400):
        print('connected but with the permanent redirect')
    elif (response.status >=400):
        print('404 NotFound')

getStatus()
