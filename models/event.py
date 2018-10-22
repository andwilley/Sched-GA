import uuid

class Event():

    def __init__(self, start, end):
        self.id = uuid.uuid4()
        self.start = start
        self.end = end
        # self.qual = qual
    
    def __repr__(self):
        return "eventId {}, start {}, end {}".format(self.id, self.start, self.end)
