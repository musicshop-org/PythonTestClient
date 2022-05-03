import requests

# Start
print("\n", "Python Test Client started.")
end = False

while not end:
    print("\n", "<Music Shop Overview>")
    print("Available commands: [s] Music search, [c] Display shopping cart, [q] Quit")
    command_valid = False

    while not command_valid:
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
                command_valid = False

                while not command_valid:
                    command = input("Enter command: ").lower()

                    # New music search
                    if command == "s":
                        print("Initiating new music search...")

                        command_valid = True

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
                        print("Back to music shop overview ...")

                        back = True
                        command_valid = True

                    # Back to music shop overview or stop client
                    elif command == "b":
                        print("Back to music shop overview ...")

                        back = True
                        command_valid = True

                    # Quit
                    elif command == "q":
                        back = True
                        command_valid = True

                    # Unknown command
                    else:
                        print("Unknown command")

                        command_valid = False

        # Shopping Cart
        elif command == "c":
            back = False
            while not back:
                print("\n", "<Shopping Cart>")
                print("Displaying shopping cart items ...")

                response = requests.get('http://localhost:8080/musicshop-1.0/api/shoppingCart/display')
                shopping_cart = response.json()

                items = shopping_cart['cartLineItems']

                if items:
                    item_count = 1

                    for item in items:
                        print("\n", "ITEM " + str(item_count))
                        print("Title:   " + item['name'])
                        print("Medium:  " + item['mediumType'])
                        print("Price:   " + str(item['price']) + " €")
                        print("Quantity:   " + str(item['quantity']))

                        item_count += 1
                        print()

                        print("Available commands: [p] Purchase line item(s), [c] Clear shopping cart, [b] Back, [q] Quit")
                        command_valid = False

                        while not command_valid:
                            command = input("Enter command: ").lower()

                            # Purchase Line Item(s)
                            if command == "p":
                                # TODO: Purchase Line Item(s)

                                command_valid = True

                        # Clear Shopping Cart
                            elif command == "c":
                                print("Clearing shopping cart ...")
                                response = requests.get('http://localhost:8080/musicshop-1.0/api/shoppingCart/clear')

                                command_valid = True

                            # Back to music shop overview or stop client
                            elif command == "b":
                                back = True
                                print("Back to music shop overview ...")

                                command_valid = True

                            # Quit
                            elif command == "q":
                                back = True
                                command_valid = True

                            else:
                                print("Unknown command")

                                command_valid = False

                else:
                    print("No items in shopping cart found. Back to music shop overview ...")

                    back = True
                    command_valid = True

        # Unknown command
        else:
            print("Unknown command")

            command_valid = False

        # Quit
        if command == "q":
            print("Stopping python test client ...")

            end = True
            command_valid = True

# End
print("\n", "Python Test Client stopped.")
