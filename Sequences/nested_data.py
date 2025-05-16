ruler = "--" * 30
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

print("My Code", ruler)
for index, (name, artist, year, songs) in enumerate(albums):
    print(f"List: {index}\t|\t"
          f"Album: {name}, "
          f"Artist: {artist}, "
          f"Year: {year}")
    for track_number, track_song in songs:
        print(f"{track_number}. {track_song}")

print("Code below are from Udemy", ruler)
for index, (name, artist, year, songs) in enumerate(albums):
    print(f"Position: {index}\t|\t"
          f"Album: {name}, "
          f"Artist: {artist}, "
          f"Year: {year}",
          f"Songs: {songs}")

print()

print("Get the song Keeping a Rendezvous", ruler)
# select album
album = albums[2]
print(album)
# get songs from an album
songs = album[3]
print(songs)
# get specific song from the list of songs
song = songs[1]
print(song)
print(song[1])

print("Get the song Mayhem", ruler)
# get an album
album = albums[3]
print(album)
# get songs from an album
songs = album[3]
print(songs)
# get specific song from the list of songs
song = songs[2]
print(song)
print(song[1])

mayhem = albums[3][3][2][1]
print(mayhem)
