import uuid
from uuid import UUID

class Pilot():

    def __init__(self) -> None:
        self.id = uuid.uuid4()

    @property
    def id(self) -> UUID:
        return self._id

    @id.setter
    def id(self, id: UUID):
        self._id = id

    def __repr__(self) -> str:
        return "pilotId {}".format(self.id.urn)
