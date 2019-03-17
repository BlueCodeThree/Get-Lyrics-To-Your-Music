# By Carlie Hamilton
# 13 March 2019
# https://github.com/BlueCodeThree
# This script allows the user to search for lyrics in the terminal

from musixmatch import Musixmatch
import apikey

musixmatch = Musixmatch(apikey.musixmatch_api)

# search for the track id
def track_id_search(q_track, q_artist):
    track_id = musixmatch.track_search(q_track, q_artist, page_size=10, page=1, s_track_rating='desc')['message']['body']['track_list'][0]['track']['track_id']
    return track_id

# get the lyrics of a song
def get_lyrics(track_id):
    lyrics = musixmatch.track_lyrics_get(track_id)['message']['body']['lyrics']['lyrics_body']
    return lyrics

# User enters the song (track) name and the artist's name
print("Please enter the Song Name:")
track_name = input(" ")
print("Please enter the Artist Name:")
track_artist = input(" ") 

# Terminal prints out the track ID and the lyrics
while True:
    try:
        print(" ")
        print(" ")
        print("Lyrics: ")
        print(get_lyrics(track_id_search(track_name, track_artist)))
        break
    except IndexError:
        print(" ")
        print("OOPS!")
        print("Your search brought up no results. Please try again!")
        print("Please enter the Song Name:")
        track_name = input(" ")
        print("Please enter the Artist Name:")
        track_artist = input(" ") 
