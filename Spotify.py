# This is a library containing the Spotify Web API.
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# The Client ID and Secret can be found from your dashboard page.
client_id = ''
client_secret = ''

# Authenticate with the Spotify API.
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


# This function is used to search for songs on Spotify.
def search_spotify_song(song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    songs = results['tracks']['items']
    return songs


# This function will be used to add a song to the playlist file.
# The file and song will equate to playlist and results[] later on. Taking two string inputs.
def add_song_to_playlist(file, song):
    # Using a for append.
    with open(file, 'a') as f:
        # Print the name of the song.
        print(song['name'])
        # Print the Spotify URI of the song.
        print(song['uri'])
        print()
        # Write the song into the playlist file.
        f.write(song['name'] + '\n')
        f.write(song['uri'] + '\n\n')


# This is the main function.
def run():
    # This will allow the user to input the name of the playlist that will be saved as a text file.
    playlist_name = input("\nPlease enter the name of your playlist: ")
    playlist = f'{playlist_name}.txt'

    # We are using a loop to present the user a menu allowing them to add songs upto when they want to exit.
    while True:

        print("\nMenu: ")
        print("a. Add a song")
        print("x. Exit")

        # We capture the user's input and change it to lowercase.
        choice = input("\nEnter your choice: ").lower()

        if choice == 'a':
            # Store user's input.
            song_name = input("\nEnter a song name: ")

            # We call the function search_spotify_song to return the Spotify song data for the input.
            results = search_spotify_song(song_name)

            # There are no songs found within the Spotify API database with that name.
            if not results:
                print(f"\nNo search results found for {song_name}")
            else:
                # Call the function to add the song into the named playlist.
                add_song_to_playlist(playlist, results[0])
        elif choice == 'x':
            # User chose to exit
            print("\nExiting the program. Goodbye!")
            break
        else:
            # Validate user input.
            print("\nInvalid choice. Please enter a valid option.")


# Call the function to run the program.
run()