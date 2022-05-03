import requests


# Start
print("\n", "Python Test Client started.")

while True:
    print("\n", "<Music Shop Overview>")
    print("Available commands: [s] Music search, [c] Display shopping cart, [q] Quit")

    command = input("Enter command: ").lower()

    # Music Search
    if command == "s":
        back = False
        while not back:
            print("\n", "<Music Search>")

            song_title = input("Enter song title: ")

            print("Searching for albums containing a song with title '" + song_title.upper() + "' ...")

            response = requests.get('http://localhost:8080/musicshop-1.0/api/albums/' + song_title)
            albums = response.json()

            album_count = 1

            for album in albums:

                print("\n", "ALBUM " + str(album_count))
                print("Title:   " + album['title'])
                print("Medium:  " + album['mediumType'])
                print("Price:   " + str(album['price']) + " €")
                print("Stock:   " + str(album['stock']))

                print("\n", "SONGS OF ALBUM " + str(album_count))

                song_count = 1

                for song in album['songs']:
                    print('#' + str(song_count) + ' ' + song['title'])

                    for artist in song['artists']:
                        print(artist['name'])

                    song_count += 1

                album_count += 1
                print()

            print("Available commands: [a] Add album(s) to shopping cart, [s] New music search, [b] Back, [q] Quit")
            command = input("Enter command: ").lower()

            # New music search
            if command == "s":
                print("Initiating new music search...")

            # Add album(s) to shopping cart
            elif command == "a":
                album_number = input("Enter album number: ")
                quantity = input("Enter quantity: ")
                album = albums[int(album_number) - 1]

                req = {
                    "title": album['title'],
                    "mediumType": album['mediumType'],
                    "price": album['price'],
                    "stock": album['stock'],
                    "quantityToAddToCart": quantity
                }

                response = requests.post('http://localhost:8080/musicshop-1.0/api/albums/addToCart', json=req)

                # add search result to cart
                print("\n", "ALBUM " + album_number)
                print("Album: " + album['title'])
                print("Medium: " + album['mediumType'])
                print("Quantity: " + quantity)
                print("Added to cart.")

                back = True

            # Back to music shop overview or stop client
            elif command == "b":
                back = True
                print("Back to music shop overview ...")

            elif command == "q":
                back = True
                print("Stopping python test client ...")

            # Unknown command
            else:
                print("Unknown command. Initiating new music search ...")

    # Shopping Cart
    elif command == "c":
        print("\n", "<Shopping Cart>")

        response = requests.get('http://localhost:8080/musicshop-1.0/api/shoppingCart/display')
        shopping_cart = response.json()

        print(shopping_cart)

    # Unknown command
    else:
        print("Unknown command")

    # Quit
    if command == "q":
        break

# End
print("\n", "Python Test Client stopped.")
