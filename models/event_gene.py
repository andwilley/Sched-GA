class EventGene():

    def __init__(self, event_id: str) -> None:
        self.event_id = event_id
        self.pilot_id = None

    @property
    def event_id(self) -> str:
        return self._event_id

    @event_id.setter
    def event_id(self, event_id: str):
        self._event_id = event_id

    @property
    def pilot_id(self) -> str:
        return self._pilot_id

    @pilot_id.setter
    def pilot_id(self, pilot_id: str):
        self._pilot_id = pilot_id

    def __repr__(self):
        return "event_id {}, pilot_id {}".format(self.event_id, self.pilot_id)
        