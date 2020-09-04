from SongCollection import SongCollection
import datetime

song_collection = SongCollection()


def add_song():
    title = validate_string("title")
    artist = validate_string("artist/band name")
    year_purchased = validate_int("year purchased", "Please enter a year purchased: ",
                                  0, datetime.datetime.now().year)
    category = validate_string("category")
    song_collection.add_song(title, artist, year_purchased, category)


def display_songs():
    if song_collection.get_song_list_len() == 0:
        print("No songs in collection.")
    song_collection.display_songs()


def display_by_artist():
    artist = validate_string("artist/band name")
    songs_by_artist = song_collection.get_song_by_artist(artist)
    if len(songs_by_artist) == 0:
        print("No songs by artist/band.")
    for songs in songs_by_artist:
        print(songs)


def delete_song():
    title = validate_string("title")
    title = song_collection.get_song_by_title(title)
    delete = song_collection.delete_song(title)
    if delete:
        print("Song deleted.")
    else:
        print("No such song in collection.")


def validate_string(string_input):
    string = input("Please enter " + string_input + ": ")
    while string == "" or len(string.strip()) <= 0 \
            or len(string.strip()) >= 200:
        string = input("Please enter valid " + string_input + ": ")
    string = string.strip()
    return string


def validate_int(int_name, prompt, lower_limit, upper_limit):
    valid_int = False
    while not valid_int:
        try:
            num = int(input(str(prompt)))
            if num <= lower_limit or num > upper_limit:
                print("Enter a valid " + int_name + ".")
            else:
                valid_int = True
                return num
        except ValueError:
            print(int_name.title() + " must be an int.")


print("Welcome to your song collection! Please choose one of the following instructions:")
while True:
    option = 0
    option = validate_int("option", "1. Add a new song\n2. Display all songs\n3. Select and display"
                                    " songs by artist/band\n4. Delete song\n5. Exit\n", 0, 5)
    if option == 1:
        add_song()
    elif option == 2:
        display_songs()
    elif option == 3:
        display_by_artist()
    elif option == 4:
        delete_song()
    elif option == 5:
        exit()
