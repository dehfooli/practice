from Media import MeidaClass

class Series(MeidaClass):
    def __init__(self, count,episode,*args):
        self.count = count
        self.episode = episode
        super().__init__(*args)
