import uuid
from uuid import UUID

class Pilot():

    def __init__(self, callsign: str = '') -> None:
        self.id = uuid.uuid4()
        self.callsign = callsign

    @property
    def id(self) -> UUID:
        return self._id

    @id.setter
    def id(self, the_id: UUID):
        self._id = the_id

    @property
    def callsign(self) -> str:
        return self._callsign

    @callsign.setter
    def callsign(self, callsign: str) -> None:
        self._callsign = callsign

    def __repr__(self) -> str:
        return "pilotId {}".format(self.id.urn)
