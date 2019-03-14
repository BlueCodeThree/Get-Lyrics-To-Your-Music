# By Carlie Hamilton
# 13 March 2019
# https://github.com/BlueCodeThree
# Grabs the song spotify is currently playing and shows you the lyrics to it. 

import spotipy
import spotipy.util as util
import apikey
import sys
import json
import webbrowser
import os
from json.decoder import JSONDecodeError

username = apikey.spotify_username
scope = 'user-read-currently-playing'

# getting a token
try:
    token = util.prompt_for_user_token(username,scope,client_id=apikey.spotify_id,client_secret=apikey.spotify_secret,redirect_uri=apikey.spotify_redirect)
except:
    print("Can't get token for", username)
    os.remove(f".cache-{username}")
    token = token = util.prompt_for_user_token(username,scope,client_id=apikey.spotify_id,client_secret=apikey.spotify_secret,redirect_uri=apikey.spotify_redirect)


# spotify object
sp = spotipy.Spotify(auth=token)

current_playing_artist = sp.current_user_playing_track()['item']['album']['artists'][0]['name']
print("Artist = " + current_playing_artist)

current_playing_song = sp.current_user_playing_track()['item']['name']
print("Song = " + current_playing_song)

