import random


# Import the random module for class player, metod next


# Define a Track class for representing music tracks
class Track:
    def __init__(self, name: str, duration: int, artist: str, is_played: bool = False):
        self.name = name
        # Check if the duration is valid (greater than 0 and not infinity)
        if 0 < duration < float('inf'):
            self.duration = duration
        else:
            raise ValueError('invalid track duration')
        self.artist = artist
        self.is_played = False

    def __repr__(self):
        # String representation of the Track object
        return f'{self.name}:{self.duration}'

    def play(self):
        # Mark the track as played
        self.is_played = True

    def stop(self):
        self.is_played = False


class Commercial(Track):
    # Define a Commercial class, which is a subclass of Track
    def __init__(self, artist: str):
        # Initialize a commercial track with default values
        super().__init__('commercial', 60, artist)

    def play(self):
        super().play()
        # Override the play method to display a message about the artist
        print(f'for more songs by {self.artist}, go to GoodVibes website')


class Player:
    # Define a Player class for managing a list of tracks
    def __init__(self, tracks: list):
        self.list_of_tracks = tracks
        # Store the list of tracks
        list_of_artist = []
        # Extract artist names from the tracks
        for track in tracks:
            list_of_artist.append(track.artist)
        # Create a set of unique artist names
        list_of_artist = set(list_of_artist)
        # Add commercial tracks for each unique artist
        for artist in list_of_artist:
            self.list_of_tracks.append(Commercial(artist))
        # Initialize the current track to -1
        self.current = - 1

    def next(self, rand: bool = False):
        # Stop the currently playing track (if there is one)
        if self.current != -1:
            self.list_of_tracks[self.current].stop()
        # Choose the next track randomly if rand is True
        if rand:
            self.current = random.randint(0, len(self.list_of_tracks) - 1)
        else:
            # Increment the current track index (looping to the beginning if necessary)
            self.current = (1 + self.current) % len(self.list_of_tracks)
        # Play the selected track

        self.list_of_tracks[self.current].play()
