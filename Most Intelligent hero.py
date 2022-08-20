import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url).json()
intelligences = {hero['name']: hero['powerstats']['intelligence']
                for hero in response
                if hero['name'] == 'Hulk'
                or hero['name'] == 'Captain America'
                or hero['name'] == 'Thanos'}
for hero in response:
    if hero['name'] in intelligences \
            and \
            hero['powerstats']['intelligence'] == max(intelligences.values()):
        most_intelligent = hero['name']
        print(f'Самый умный: {most_intelligent}')
