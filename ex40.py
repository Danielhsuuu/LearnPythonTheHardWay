class Song(object):
    
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

despacito = Song(["¡Oh!",
                  "Tú, tú eres el imán y yo soy el metal",
                  "Me voy acercando y voy armando el plan",
                  "Sólo con pensarlo se acelera el pulso (¡Oh, yeah!)"])

babysharklyrics = ["Baby shark, doo doo doo doo doo doo", "Baby shark, doo doo doo doo doo doo", "Baby shark, doo doo doo doo doo doo"]

baby_Shark = Song(babysharklyrics)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

despacito.sing_me_a_song()

baby_Shark.sing_me_a_song()