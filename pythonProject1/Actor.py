from Media import MeidaClass

class Actor(MeidaClass):
    def __init__(self, firstname,lastname,birthdate,gender):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.gender = gender
