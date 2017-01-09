#--------|---------|---------|---------|---------|---------|---------|---------
# Kill Nickelback

# In this exercises, you're going to use a conditional statement inside a comprehension. Let's look at a basic example.

## Instructions

# 1. Define a set that contains tuples. Each tuple should contain two strings:
#     1. The name of an artist
#     1. A song by that artist

#     Make sure that some of the songs are from the band Nickelback. You can see a [list of their greatest hits](https://www.amazon.com/Best-Nickelback-1/dp/B00FFERTUK/) on Amazon.

songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals'),
    ('Thelonious Monk', 'Round Midnight'),
    ('Phish', 'You Enjoy Myself')
}

good_songs = [song for song in songs if song[0] != 'Nickelback']
print(good_songs)

# 1. Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.
