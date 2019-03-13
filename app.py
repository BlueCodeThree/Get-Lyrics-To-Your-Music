from musixmatch import Musixmatch
import apikey

musixmatch = Musixmatch(apikey.api)

# search for the track id
def track_id_search(q_track, q_artist):
    track_search = musixmatch.track_search(q_track, q_artist, page_size=10, page=1, s_track_rating='desc')['message']['body']['track_list'][0]['track']['track_id']
    return track_search
    #for k, v in track_search['track']:
    #    return k, v

print(track_id_search("The Safety of Disbelief", "Light the Torch"))

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





