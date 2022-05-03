import requests


def music_search():

    print()
    print("Enter a song title of an album you are interested in")
    song_title = input("song title: ")

    response = requests.get('http://localhost:8080/musicshop-1.0/api/albums/' + song_title)
    albums = response.json()

    album_count = 1

    for album in albums:

        print()
        print("ALBUM " + str(album_count))
        print("Title:   " + album['title'])
        print("Medium:  " + album['mediumType'])
        print("Price:   " + str(album['price']) + " €")
        print("Stock:   " + str(album['stock']))

        print()
        print("SONGS OF ALBUM " + str(album_count))

        song_count = 1

        for song in album['songs']:
            print('#' + str(song_count) + ' ' + song['title'])

            for artist in song['artists']:
                print(artist['name'])

            song_count += 1

        album_count += 1
        print()

    return albums


def add_to_cart(albums):

    album_number = input("number: ")
    quantity = input("quantity: ")
    album = albums[int(album_number)-1]

    req = {
        "title": album['title'],
        "mediumType": album['mediumType'],
        "price": album['price'],
        "stock": album['stock'],
        "quantityToAddToCart": quantity
    }

    response = requests.post('http://localhost:8080/musicshop-1.0/api/albums/addToCart', json=req)

    # add search result to cart
    print()
    print("Album: " + album['title'])
    print("Medium: " + album['mediumType'])
    print("Quantity: " + quantity)
    print("added to cart!")


def user_action():

    print()
    print("What would you like to do next?")
    print()
    print("1 -> add searched album/s to cart")
    print("2 -> search for another album")
    print("3 -> quit")
    print()
    action = input("choose action: ")
    return action


def start_client():

    print()
    print("Welcome to our music shop! :)")
    chosen_action = '2'
    quit = 1

    while quit > 0:
        if chosen_action == '1':
            add_to_cart(albums)
            chosen_action = user_action()
        elif chosen_action == '2':
            albums = music_search()
            chosen_action = user_action()
        elif chosen_action == '3':
            quit = 0
        else:
            print()
            print("wrong input try again")
            chosen_action = user_action()


start_client()

