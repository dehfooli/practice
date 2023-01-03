from Media import MeidaClass

class Film(MeidaClass):
    def __init__(self, type,*args):
        self.type = type
        super().__init__(*args)
