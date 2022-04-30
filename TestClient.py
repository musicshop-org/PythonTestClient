import requests
import json

# Greeting
print()
print("Welcome to our music shop! :)")

# Search
print()
print("Enter a song title of an album you are interested in")
songTitle = input("song title: ")

response = requests.get('http://localhost:8080/musicshop-1.0/api/albums/' + songTitle)
albums = response.json()

albumCount = 1

for album in albums:
    print()
    print("ALBUM " + str(albumCount))
    print("Title:   " + album['title'])
    print("Medium:  " + album['mediumType'])
    print("Price:   " + str(album['price']) + " €")
    print("Stock:   " + str(album['stock']))

    print()
    print("SONGS OF ALBUM " + str(albumCount))

    songCount = 1

    for song in album['songs']:
        print('#' + str(songCount) + ' ' + song['title'])

        for artist in song['artists']:
            print(artist['name'])

        songCount += 1

    albumCount += 1
    print()


# User Options
# print("What would you like to do next?")
# print()
# print("1 -> add searched album/s to cart")
# print("2 -> search for another album")
# print("3 -> quit")
# print()