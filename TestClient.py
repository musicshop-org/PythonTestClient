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
            songTitle = input("Enter song title: ")

            print("Searching for albums containing a song with title '" + songTitle.upper() + "' ...")
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

            print("Available commands: [a] Add album(s) to shopping cart, [s] New music search, [b] Back, [q] Quit")
            command = input("Enter command: ").lower()

            # New music search
            if command == "s":
                print("Initiating new music search...")

            # Add album(s) to shopping cart
            elif command == "a":
                # TODO: functionality to add displayed album(s) to shopping cart
                print("TODO: functionality to add displayed album(s) to shopping cart")

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

    # Unknown command
    else:
        print("Unknown command")

    # Quit
    if command == "q":
        break

# End
print("\n", "Python Test Client stopped.")
