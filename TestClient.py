import requests

# Start
print("\n", "Python Test Client started ...")

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
                continue

            # Back to music shop overview or stop client
            if command == "b" or command == "q":
                back = True

            # Add album(s) to shopping cart
            elif command == "a":
                print("Do something")

            # Unknown command
            else:
                # TODO: handle unknown command
                print("Unknown command")

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
print("\n", "Python Test Client stopped ...")
