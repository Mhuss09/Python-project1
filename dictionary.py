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
    playlist[title] = {
        "artist": artist,
        "genre": genre
    }

def view_playlist():
    print(playlist)

def update_song(title, artist, genre):
    playlist[title] = {
        "artist": artist,
        "genre": genre
    }

def delete_song(title):
    if title in playlist:
        del playlist[title]

add_song("Waka Waka", "Shakira", "Pop")
view_playlist()

update_song("Waka Waka", "NotShakira", "Rock")
view_playlist()

delete_song("Waka Waka")
view_playlist()