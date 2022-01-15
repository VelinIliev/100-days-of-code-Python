import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"

# date = input("Type date (YYYY-MM-DD): ")
date = "1997-04-29"

print(f"{URL}{date}/")

response = requests.get(f"{URL}{date}/")
content = response.text

soup = BeautifulSoup(content, "html.parser")

selector = ".chart-results-list .o-chart-results-list-row-container .lrv-u-width-100p #title-of-a-story"

song_names_tmp = soup.select(selector)

songs_names = [item.text.strip() for item in song_names_tmp ]

arist_names_tmp = soup.select(f"{selector}~span") 

arist_names = [item.text.strip() for item in arist_names_tmp ]

with open("top songs.txt", mode="w") as file:
    file.write(f'{date}\n')
    count = 0
    for n in range(0,len(songs_names)):
        count += 1
        file.write(f'{count}. {songs_names[n]} ({arist_names[n]})\n')

SPOTIFY_CLIENT_ID = "************************"
SPOTIFY_CLIENT_SECRET = "************************"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id= SPOTIFY_CLIENT_ID,
        client_secret= SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]

for song in songs_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"{song}")
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)