import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#music_date = input("which year do you want to travel to? type the date in this format YYYY-mm-dd: ")
BILLBOARD_URL = f"https://music.apple.com/us/playlist/top-100-usa/pl.606afcbb70264d2eb2b51d8dbcfa6a12"
CLIENT_ID = "b79df62b9e0a415e90ba405e93f79869"
CLIENT_SECRET = "7f534fafdb614ddbbda1541fd7a4b3cb"


response = requests.get(url=BILLBOARD_URL).text


soup = BeautifulSoup(response, "html.parser")
music_names = soup.find_all(name="div",class_="songs-list-row__song-name")
name_list = [ name.getText() for name in music_names][0:10] 


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id=sp.current_user()['id']
create_playlist = sp.user_playlist_create(user=user_id, name="Top 10: Apple Musiz", public=False)["id"]
song_uris = []

for name in name_list:
    try:
        songs = sp.search(q=f"track:{name}")
        uris = (songs["tracks"]["items"][0]["uri"])
        song_uris.append(uris)
        
    except IndexError:
        print(f"{name} was not found in Spotify")


sp.playlist_add_items(playlist_id=create_playlist, items=song_uris) 