import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
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

def get_recommended_tracks(track_ids: list[str], limit: int = 10):
    seed_tracks = track_ids[:5]  # Spotify는 최대 5곡까지만 seed로 허용

    recommendations = sp.recommendations(
        # seed_tracks=seed_tracks,
        # seed_genres=["pop"],
        seed_artists=["4NHQUGzhtTLFvgF5SZesLK"],
        seed_genres=["classical", "country"],
        seed_tracks=["0c6xIDDpzE81m2q797ordA"],
        limit=1
    )
    # print(recommendations)

    tracks = []
    for rec in recommendations["tracks"]:
        title = rec["name"]
        artist = rec["artists"][0]["name"]
        track_id = rec["id"]
        album_image = rec["album"]["images"][0]["url"]

        tracks.append({
            "title": title,
            "artist": artist,
            "track_id": track_id,
            "album_image": album_image
        })

    return tracks
