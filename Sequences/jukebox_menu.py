from nested_data2 import albums
from inspect_line import print_ruler

ruler_switch = True

SONGS_LIST = 3
SONG_TITLE_INDEX = 1

while True:
    print("Displaying albums available:\n")
    # unpack the album
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"Album #{index + 1}: {title}")
    print_ruler(ruler_switch)

    # initialize
    min_valid = 1
    max_valid = len(albums)

    album_choice = int(input("Please choose your album (invalid choice exits): "))

    # list of songs containing (track number, song name) from selected album
    if min_valid <= album_choice <= max_valid:
        songs_list = albums[album_choice -1][SONGS_LIST]
    else:
        break

    print("Please choose your song:" )
    # unpack the list of songs from the album
    for index, (track_number, song) in enumerate(songs_list):
        print(f"{index + 1}: {song}")

    song_max_valid = len(songs_list)
    song_choice = int(input())
    if min_valid <= song_choice <= song_max_valid:
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print(f"Playing {title}")

    print_ruler()
