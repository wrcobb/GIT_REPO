class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
            
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
                   
bulls_lyrics = ["They rally around the family",
                "With pockets full of shells"]

bulls_on_parade = Song(bulls_lyrics)
                        
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

