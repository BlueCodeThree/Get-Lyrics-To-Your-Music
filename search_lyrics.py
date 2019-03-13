# By Carlie Hamilton
# 13 March 2019
# This script allows the user to search for lyrics in the terminal

from musixmatch import Musixmatch
import apikey

musixmatch = Musixmatch(apikey.api)

# search for the track id
def track_id_search(q_track, q_artist):
    track_id = musixmatch.track_search(q_track, q_artist, page_size=10, page=1, s_track_rating='desc')['message']['body']['track_list'][0]['track']['track_id']
    return track_id

# get the lyrics of a song
def get_lyrics(track_id):
    lyrics = musixmatch.track_lyrics_get(track_id)['message']['body']['lyrics']['lyrics_body']
    return lyrics

print("Please enter the Track Name:")
track_name = input(" ")
print("Please enter the Artist Name:")
track_artist = input(" ") 

print("Track Id:" + str(track_id_search(track_name, track_artist)))
print(" ")
print("Lyrics: ")
print(get_lyrics(track_id_search(track_name, track_artist)))




# url = "https://api.musixmatch.com/ws/1.1/track.lyrics.get?format=jsonp&callback=callback&track_id=148791234&apikey=" + apikey.api

# uh = urllib.request.urlopen(url)
# data = uh.read()
# print ('Retrieved',len(data),'characters')

# data_string = data.decode("utf-8")
# js = json.loads(data_string)

#open_url = urllib.request.urlopen(url).read() 
#result = open_url.decode("utf8")
#print(result)

# response = requests.get(url).json()
# print(type(response))
# print(response)





