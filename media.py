from Actors import Actors
import pytube

class Media:
    def __init__(self,id,n,c,r,u,d,cs):
        self.id = id
        self.name = n
        self.category = c
        self.IMDB_rate = r
        self.url = u
        self.duration = d
        self.casts = cs

    def show_info(self):
        print(f"media name: {self.name} --- category: {self.category}")

    
    def show_casts(self):
        actor = self.casts.split('-')
        for i in actor:
            Actors(i).actors()

    def download_media(self):
        pytube.YouTube(self.url).streams.first().download()
            