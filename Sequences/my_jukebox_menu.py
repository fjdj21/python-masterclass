from nested_data2 import albums
from inspect_line import print_ruler

ruler_switch = True

# CONSTANTS

SONGS_LIST = 3
ALBUM_NAME = 0


while True:
    print("Displaying albums available:\n")
    # unpack the album
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"Album #{index + 1}: {title}")
    print_ruler(ruler_switch)

    # initializers
    min_valid = 1
    max_valid = len(albums)

    # handle input for album
    try:
        album_choice = int(input("Please choose your album (invalid choice exits): "))
        # check if album choice is valid
        if min_valid <= album_choice <= max_valid:
            album_name = albums[album_choice - 1][ALBUM_NAME]
            songs_list = albums[album_choice - 1][SONGS_LIST]

            print(f"You chose the album: {album_name}")
            print_ruler(ruler_switch)

            # handle input for song
            while True:
                # list of songs from selected album
                for index, (track_number, track_song) in enumerate(songs_list):
                    print(f"Song #{index + 1}: {track_song}")
                try:
                    print_ruler(ruler_switch)
                    song_choice = int(input("Please select a song: "))
                    # initialize
                    song_max_valid = len(songs_list)

                    # check if the song choice is valid
                    if min_valid <= song_choice <= song_max_valid:
                        track_number_index, song_name = songs_list[song_choice - 1]
                        print(f"You are playing: [{track_number_index}. {song_name}]")

                        # ask the user to continue
                        cont = input("Would you like to choose another album? (y/n): ").strip().lower()
                        if cont == 'y':
                            break # valid song choice, break the loop
                        else:
                            print("Goodbye!")
                            exit()
                        print_ruler(ruler_switch)
                    else:
                        total_songs = len(songs_list)
                        print(f"Invalid choice, please choose from songs 1 to {total_songs}")
                except ValueError:
                    print("Please enter a valid number for song, try again")
        else:
            total_albums = max_valid
            print(f"Invalid choice, please choose from albums 1 to {total_albums}")
    except ValueError:
        print("Please enter a valid number for album, try again")
        print_ruler(ruler_switch)
