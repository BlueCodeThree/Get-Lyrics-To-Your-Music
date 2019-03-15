# By Carlie Hamilton
# 15 March 2019
# https://github.com/BlueCodeThree
# Top tracks and top artists that you've been listening to lately. 

import spotipy
import spotipy.util as util
import apikey
import sys
import webbrowser
import os

username = apikey.spotify_username
scope = 'user-top-read'

# getting a token
try:
    token = util.prompt_for_user_token(username,scope,client_id=apikey.spotify_id,client_secret=apikey.spotify_secret,redirect_uri=apikey.spotify_redirect)
except:
    print("Can't get token for", username)
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id=apikey.spotify_id,client_secret=apikey.spotify_secret,redirect_uri=apikey.spotify_redirect)


# spotify object
sp = spotipy.Spotify(auth=token)


# Get users top tracks
print("Top Tracks")
top_tracks = sp.current_user_top_tracks(limit=10, offset=0, time_range='medium_term')
for i, track in enumerate(top_tracks['items']):
    # track_name = top_tracks['name']
    # track_artist = top_tracks['artists'][0]['name']
    print(i + 1, track['name'], " by ", track['artists'][0]['name'])
    
print(" ")

# get user's top artists
print("Top Artists")
results = sp.current_user_top_artists(time_range='medium_term', limit=10)
for i, item in enumerate(results['items']):
    print(i + 1, item['name'])
