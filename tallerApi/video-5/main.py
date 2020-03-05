import requests
import json

if __name__ == '__main__':
    #https://httpbin.org/get?nombre=Jonathan%20Guevara%20Torres
    url = 'https://httpbin.org/post'
    payload ={'nombre': 'Jonathan', 'nivel': 'Dios' }

    response = requests.post(url, data=json.dumps(payload))
    #json post se encarga de serializarlos
    print(response.url)

    if response.status_code == 200:
        print(response.content)

    
