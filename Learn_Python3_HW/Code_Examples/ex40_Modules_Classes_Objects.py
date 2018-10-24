class Song(object):
    # create a song object and takes in a list item that contains the song lines
    def __init__(self, lyrics):
        self.lyrics = lyrics

    # prints each element in song. Which is one line of the song
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

hb = ["Happy birthday to you",
     "I don't want to get sued",
    "So I'll stop right there"]

happy_bday = Song(hb)

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print(happy_bday.lyrics)
