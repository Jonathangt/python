import requests

if __name__ == '__main__':
    url = 'https://www.youtube.com/'
    response = requests.get(url)
    print(response)#imprimo el status code

    if response.status_code == 200:
        content = response.content
        file = open('youtube.html', 'wb')
        file.write(content)
        file.close
