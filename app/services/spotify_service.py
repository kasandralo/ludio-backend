import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_track_info(track_id: str):
    track = sp.track(track_id)
    title = track["name"]
    artist = track["artists"][0]["name"]
    album_image = track["album"]["images"][0]["url"]
    return {
        "title": title,
        "artist": artist,
        "album_image": album_image
    }
