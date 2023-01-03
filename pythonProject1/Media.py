from pytube import YouTube
class MeidaClass():
    def __init__(self, name, director,imdb_score,url,duration,casts):
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.casts = casts

    def showinfo(self):
        return [{property:value for property, value in vars(self).items()}]

    def download(self):
        # 1
        # return YouTube('https://youtu.be/%s' %(self.url)).streams.first().download()
        # 2
        yt = YouTube('http://youtube.com/%s' %(self.url))
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        return "Done!"


class Media:
    pass