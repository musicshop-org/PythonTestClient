import requests
import json

def musicSearch():
    # Search
    print()
    print("Enter a song title of an album you are interested in")
    songTitle = input("song title: ")

    response = requests.get('http://localhost:8080/musicshop-1.0/api/albums/' + songTitle)
    albums = response.json()

    print(response.json())

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

    return albums

def addToCart(albums):
    albumNumber = input("number: ")
    dictionary = {
        "name": "achim"
    }
    dictionary = json.dumps(dictionary)
    album = json.dumps(albums[int(albumNumber)-1])

    response = requests.post('http://localhost:8080/musicshop-1.0/api/test1', json=album)
    print(response)
    response = requests.post('http://localhost:8080/musicshop-1.0/api/albums/addToCart', json=album)
    print(response)

    # add search result to cart
    albumNumber = int(albumNumber) - 1
    print("Album: " + albums[albumNumber]['title'])
    print("Medium: " + albums[albumNumber]['mediumType'])
    print("added to cart!")
    print()

def userAction():
    print()
    print("What would you like to do next?")
    print()
    print("1 -> add searched album/s to cart")
    print("2 -> search for another album")
    print("3 -> quit")
    print()
    action = input("choose action: ")
    return action

def startClient():
    # Greeting
    print()
    print("Welcome to our music shop! :)")
    choosenAction = '2'
    quit = 1

    while quit > 0:
        if choosenAction == '1':
            addToCart(albums)
            choosenAction = userAction()
        elif choosenAction == '2':
            albums = musicSearch()
            choosenAction = userAction()
        elif choosenAction == '3':
            quit = 0
        else:
            print()
            print("wrong input try again")
            choosenAction = userAction()

#start Client
startClient()

