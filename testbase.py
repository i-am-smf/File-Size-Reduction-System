import requests

Get_players = requests.get(f'http://157.254.166.75:30120/info.json', timeout=20)

# Get_players = get(f'http://51.79.181.126:30129/players.json', timeout=5)

print(Get_players.content)