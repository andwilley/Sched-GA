class EventGene():

    def __init__(self, eventId):
        self.eventId = eventId
        self.pilotId = None

    def __repr__(self):
        return "eventId {}, pilotId {}".format(self.eventId, self.pilotId)
        