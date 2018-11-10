import uuid

class EventGene():

    def __init__(self, event_id: uuid.UUID) -> None:
        self.event_id = event_id
        self.pilot_id = None

    @property
    def event_id(self) -> uuid.UUID:
        return self._event_id

    @event_id.setter
    def event_id(self, event_id: uuid.UUID):
        self._event_id = event_id

    @property
    def pilot_id(self) -> uuid.UUID:
        return self._pilot_id

    @pilot_id.setter
    def pilot_id(self, pilot_id: uuid.UUID):
        self._pilot_id = pilot_id

    def copy(self) -> 'EventGene':
        gene = EventGene(self.event_id)
        gene.pilot_id = self.pilot_id
        return gene

    def __repr__(self):
        return "event_id {}, pilot_id {}".format(self.event_id, self.pilot_id)
