albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budge", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
] # packed tuple inside a list

ruler = "--" * 50

print(len(albums))

for album in albums:
    print(f"Album: {album[0]}, "
          f"Artist: {album[1]}, "
          f"Year: {album[2]}")

print("Approach 1", ruler)
# Approach 1: For loop to unpack the tuple inside a list
for album in albums:
    # unpack each album index into corresponding variables
    name, artist, year = album
    print(f"Album: {name}, Artist: {artist}, Year: {year}")

print("Approach 2", ruler)
# Approach 2: For loop to unpack the tuple inside a list
# this is the recommended approach
# unpack each album index into corresponding variables
for name, artist, year in albums:
    print(f"Album: {name}, Artist: {artist}, Year: {year}")

print(ruler)
