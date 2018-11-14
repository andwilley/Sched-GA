import uuid
from typing import List
from app.models.sniv import Sniv

class Pilot():

    def __init__(self, callsign: str = '', quals: List[str] = None,
                 snivs: List[uuid.UUID] = None) -> None:
        self.id = uuid.uuid4()
        self.callsign = callsign
        self.quals = quals if quals else []
        self.snivs = snivs if snivs else []

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, the_id: uuid.UUID):
        self._id = the_id

    @property
    def callsign(self) -> str:
        return self._callsign

    @callsign.setter
    def callsign(self, callsign: str) -> None:
        self._callsign = callsign

    @property
    def quals(self) -> List[str]:
        return self._quals

    @quals.setter
    def quals(self, quals: List[str]) -> None:
        self._quals = quals


    @property
    def snivs(self) -> List[uuid.UUID]:
        return self._snivs

    @snivs.setter
    def snivs(self, snivs: List[uuid.UUID]) -> None:
        self._snivs = snivs

    def __repr__(self) -> str:
        return "pilotId {}".format(self.id.urn)
