import uuid

class Pilot():

    def __init__(self):
        self.id = uuid.uuid4()

    @property
    def id(self):
        return self.id

    def __repr__(self):
        return "pilotId {}".format(self.id)
        