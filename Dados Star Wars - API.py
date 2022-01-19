import requests

for i in range(1, 7):
    url = f'https://swapi.dev/api/planets/?format=json&page={i}'
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print(f'{url} inacessível.')
    else:
        if response.status_code == 200:
            planetas = response.json()
            for v in planetas.get('results'):
                print(f'{v["name"]}')
        else:
            print(f'Não foi possível acessar a {url}')
    