import requests
import json
import time

client_id = "05ab1e419b432931867e"
client_secret = "e13704dfe3d3f3d2f1ff8dfca0e7f51c"
data = {"client_id": client_id, "client_secret": client_secret}
resp_token = requests.post("https://api.artsy.net/api/tokens/xapp_token", data=data)
j = json.loads(resp_token.text)
token = j["token"]
headers = {"X-Xapp-Token" : token}
url = "https://api.artsy.net/api/artists/"
artists = {}
with open("problem AM.txt", "r") as string:
    total = 1
    for artist in string:
        response = requests.get(url+artist.strip(), headers=headers)
        time.sleep(0.6)
        artist_info = json.loads(response.text)
        artists[artist_info["sortable_name"]] = artist_info["birthday"]
        print(f"""{total}. {artist_info["sortable_name"]}""")
        total += 1
print(artists)
artists = sorted(artists.items(), key=lambda x: x[1])
with open("output.txt", "w", encoding='utf-8') as artists_names:
    for artist in artists:
        print(artist[1])
        artists_names.write(artist[0]+"\n")
    artists_names.write(" ")
