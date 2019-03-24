import tkinter as tk
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

# lyrics to the label
def lyrics_to_label():
    print(track_entry)
    print(artist_entry)
    print(get_lyrics(track_id_search(track_entry, artist_entry)))


HEIGHT = 500
WIDTH = 600




root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH).pack()

frame = tk.Frame(root, bg="#80c1ff")
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor="n") # relative width etc, the numbers add up to 100%

track_label = tk.Label(frame, text="Song Name:").grid(column=0, row=0)

track_entry = tk.Entry(frame, font=40).grid(column=1, row=0)

artist_label = tk.Label(frame, text="Artist Name:").grid(column=0, row=1)

artist_entry = tk.Entry(frame, font=40).grid(column=1, row=1)

button = tk.Button(frame, text="Get Lyrics", font=40, command=lyrics_to_label).grid(column=3, row=1)

lyrics_frame = tk.Frame(root, bg="pink")
lyrics_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor="n") 

lyrics_label = tk.Label(lyrics_frame, text="Lyrics here").place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)





root.mainloop()