from openapi_client.api import default_api
from openapi_client import api_client

from openapi_client.model.album_dto import AlbumDTO
from openapi_client.model.user_data_dto import UserDataDTO


def response_to_dict(data):
    dictionaries = []

    for entry in data:
        dictionaries.append(entry.to_dict())

    return dictionaries


def get_user_data():
    email_address = ""
    password = ""

    while not email_address:
        email_address = input("email: ")

    while not password:
        password = input("password: ")

    return UserDataDTO(emailAddress=email_address, password=password)


def get_authorized_rest_service(token):
    client = api_client.ApiClient()
    client.set_default_header("Authorization", token)

    return default_api.DefaultApi(client)


# Start
print()
print("Enter your credentials")
end = False
jwt_token = ""
unauthorized_rest_service = default_api.DefaultApi()

# Login
while not jwt_token:
    user_data = get_user_data()
    jwt_token = unauthorized_rest_service.login(user_data_dto=user_data)

# On successful login -> create authorized_rest_service (with Jwt-Token in Headers)
authorized_rest_service = get_authorized_rest_service(jwt_token)

print()
print("Welcome to our music shop :)")

while not end:
    print()
    print("<Music Overview>")
    print("Available commands: [s] Music search, [c] Display shopping cart, [q] Quit")
    command_valid = False

    while not command_valid:
        command = input("Enter command: ").lower()

        # Music Search
        if command == "s":
            back = False
            while not back:
                print()
                print("<Music Search>")

                song_title = input("Enter song title: ")

                print("Searching for albums containing a song with title '" + song_title.upper() + "' ...")

                response = authorized_rest_service.find_albums_by_song_title(song_title)
                albums = response_to_dict(response)

                album_count = 1

                for album in albums:

                    print()
                    print("ALBUM " + str(album_count))
                    print("Title:   " + album.get('title'))
                    print("Medium:  " + album.get('medium_type'))
                    print("Price:   " + str(album.get('price')) + " €")
                    print("Stock:   " + str(album.get('stock')))

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

                print("Available commands: [a] Add album to shopping cart, [s] New music search, [b] Back, [q] Quit")
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

                        req = AlbumDTO(
                            title=album.get('title'),
                            mediumType=album.get('medium_type'),
                            price=album.get('price'),
                            stock=album.get('stock'),
                            quantityToAddToCart=quantity
                        )

                        print("Adding ALBUM " + album_number + " to shopping cart ...")

                        authorized_rest_service.add_to_cart(album_dto=req)

                        # add search result to cart
                        print()
                        print("ALBUM " + album_number)
                        print("Title:   " + album.get('title'))
                        print("Medium:  " + album.get('medium_type'))
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
                print()
                print("<Shopping Cart>")
                print("Displaying shopping cart items ...")

                response = authorized_rest_service.display_shopping_cart()
                items = response_to_dict(response['cart_line_items'])

                if items:
                    item_count = 1

                    for item in items:
                        print()
                        print("ITEM " + str(item_count))
                        print("Title:   " + item.get('name'))
                        print("Medium:  " + item.get('medium_type'))
                        print("Price:   " + str(item.get('price')) + " €")
                        print("Quantity:   " + str(item.get('quantity')))

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
                            authorized_rest_service.clear_shopping_cart()
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
print()
print("Bye! Have a nice day :)")
