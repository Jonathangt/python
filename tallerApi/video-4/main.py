import requests
import json

if __name__ == '__main__':
    #https://httpbin.org/get?nombre=Jonathan%20Guevara%20Torres
    url = 'https://httpbin.org/get'
    args ={
        'nombre': 'Jonathan', 'nivel': 'Dios' }

    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        """
       response_json = response.json() #variable tipo diccionario
       origin = response_json['origin']
       headers = response_json['headers']
       print(origin)
       print(headers)
        """

        response_json = json.loads(response.text) #variable tipo diccionario
        origin = response_json['origin']
        headers = response_json['headers']
        print(origin)
        print(headers)

    
