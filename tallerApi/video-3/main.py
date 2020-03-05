import requests

if __name__ == '__main__':
    #https://httpbin.org/get?nombre=Jonathan%20Guevara%20Torres
    url = 'https://httpbin.org/get'
    args ={
        'nombre': 'Jonathan', 'nivel': 'Dios' }

    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        content = response.content
        print(content)
       
