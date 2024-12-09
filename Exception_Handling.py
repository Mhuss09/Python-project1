playlist = {
    "Despacito": {
        "artist": "Luis Fonsi",
        "genre": "pop"
    },
    "Shape of you": {
        "artist": "Ed Sheeran",
        "genre": "pop"
    },
    "Gangnam Style": {
        "artist": "Psy",
        "genre": "k-pop"
    }    
}


def add_song(title, artist, genre):
    try:

        if not isinstance(artist, str):
            raise ValueError("Artist must be a string.")
        playlist[title] = {
            "artist": artist,
            "genre": genre
    }
    
    except ValueError as x:
        print("Error: ", x)


def view_playlist():
    try:
        if not playlist:
            raise ValueError("The playlist is empty")
        print(playlist)
    except ValueError as x:
        print("Error ", x)

def update_song(title, artist, genre):
    try:
        if not isinstance(title, str):
            raise TypeError("Song title has to be a string")
        if not isinstance(artist, str):
            raise TypeError("Song title has to be a string")
        if title not in playlist:
            raise ValueError(title, " could not be found in the playlist...")
        playlist[title] = {
            "artist": artist,
            "genre": genre
            }
    except TypeError as x:
        print("Error", x)
    except ValueError as x:
        print("error", x)


def delete_song(title):
    try:
        if title in playlist:
            del playlist[title]
        elif title not in playlist:
            raise ValueError(title, " could not be found in the playlist...")
    except ValueError as x:
        print("error", x)


add_song("Waka Waka", 1, "Pop")

update_song("Blinding Lights", "The Weeknd", "pop")

delete_song("Shining")


playlist = {
    
}
view_playlist()