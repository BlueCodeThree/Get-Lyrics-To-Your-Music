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

# User input for the output - how many results
heading = "Your Top Tracks and Top Artists!"
print(" ")
print("-" * len(heading))
print(heading)
print("-" * len(heading))
print("This will print out your top Spotify tracks and artists")
print(" ")
print("How many results would you like? Type in a number:")
amount_results = input(" ")

# check that it is a number
while True:
    try:
        amount_results = int(amount_results)
        amount_results > 0
        break
    except:
        print(' ')
        print("OOPS!")
        print("That was not a number! Use your digits, don't type a word! ")
        print("Try again...")
        print("How many results would you like? Type in a number:")
        amount_results = input(" ")

# Finding out what time frame 
print(" ")
print("Excellent!")
print("What time range would you like to pull the data from. Type a letter:")
print("(S)hort Term - past four weeks")
print("(M)edium Term - last six months")
print("(L)ong Term - from the last several years")
timeRange = input(" ")
print(" ")
print(" ")


# Putting this input into the correct format for our output...
amount_results = int(amount_results)
while True:
    if timeRange.upper() == "S":
        time_range = "short_term"
        break
    elif timeRange.upper() == "M":
        time_range = "medium_term"
        break
    elif timeRange.upper() == "L":
        time_range = "long_term"
        break
    else:
        print(" ")
        print("You didn't type either S, M or L. Please try again!")
        print("What time range would you like to pull the data from. Type a letter:")
        print("(S)hort Term - past four weeks")
        print("(M)edium Term - last six months")
        print("(L)ong Term - from the last several years")
        timeRange = input(" ")

# Get users top tracks
top = "Top Tracks"
print("-" * len(top))
print(top)
print("-" * len(top))
top_tracks = sp.current_user_top_tracks(limit=amount_results, offset=0, time_range=time_range)
for i, track in enumerate(top_tracks['items']):
    # track_name = top_tracks['name']
    # track_artist = top_tracks['artists'][0]['name']
    print(i + 1, track['name'], " by ", track['artists'][0]['name'])
    
print(" ")

# get user's top artists
artist = "Top Artists"
print("-" * len(artist))
print(artist)
print("-" * len(artist))
results = sp.current_user_top_artists(time_range=time_range, limit=amount_results)
for i, item in enumerate(results['items']):
    print(i + 1, item['name'])
