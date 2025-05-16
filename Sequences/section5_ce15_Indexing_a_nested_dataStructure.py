"""
Practical Application of Nested Data Structure Indexing in Python
Use nested indexing to print the following items from our albums structure.

    - The title of the song "The Way I Choose" from the "Bad Company" album.
    - The year that the album "Nightflight" was released.
    - The track number of the song "Kentish Town Waltz" from the Imelda May album "More Mayhem".
    - The tuple representing the song "Keeping a Rendezvous" from the Budgie album "Nightflight".

Write your code below the comment, starting on line 42.

The output from your program should be:
    The Way I Choose
    1981
    4
    (2, 'Keeping a Rendezvous')

Print only the values requested, don't include any additional text in your output.
"""

ruler = '--' * 30
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

# Add your code below this comment.

# Get title of the song "The Way I Choose" from the "Bad Company" album
print(albums[1][3][5][1])

# Get the year that the album "Nightflight" was released
print(albums[2][2])

# Get the track number of the song "Kentish Town Waltz" from the
# Imelda May album "More Mayhem".
print(albums[3][3][3][0])

# Get the tuple representing the song "Keeping a Rendezvous"
# from the Budgie album "Nightflight".
print(albums[2][3][1])
