# By Carlie Hamilton
# 13 March 2019
# https://github.com/BlueCodeThree
# Grabs the song spotify is currently playing and shows you the lyrics to it. 

import spotipy
import spotipy.util as util
import apikey
import sys
import webbrowser
import os
from musixmatch import Musixmatch

username = apikey.spotify_username
scope = 'user-read-currently-playing'
musixmatch = Musixmatch(apikey.musixmatch_api)

# getting a token
try:
    token = util.prompt_for_user_token(username,scope,client_id=apikey.spotify_id,client_secret=apikey.spotify_secret,redirect_uri=apikey.spotify_redirect)
except:
    print("Can't get token for", username)
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id=apikey.spotify_id,client_secret=apikey.spotify_secret,redirect_uri=apikey.spotify_redirect)


# spotify object
sp = spotipy.Spotify(auth=token)

# Gets the currently playing artist and song name
current_playing_artist = sp.current_user_playing_track()['item']['album']['artists'][0]['name']
print("Artist: " + current_playing_artist)
current_playing_song = sp.current_user_playing_track()['item']['name']
print("Song: " + current_playing_song)

# search for the track id - in order to get the lyrics
track_id = musixmatch.track_search(current_playing_song, current_playing_artist, page_size=10, page=1, s_track_rating='desc')['message']['body']['track_list'][0]['track']['track_id']

# get the lyrics of a song
def get_lyrics(track_id):
    lyrics = musixmatch.track_lyrics_get(track_id)['message']['body']['lyrics']['lyrics_body']
    return lyrics

# Terminal prints out the lyrics
print("Lyrics: ")
print(get_lyrics(track_id))

