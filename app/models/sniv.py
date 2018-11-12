import uuid
from datetime import datetime

class Sniv:

    def __init__(self, start: datetime, end: datetime, pilot_id: uuid.UUID, desc: str = ''):
        self.id = uuid.uuid4()
        self.start = start
        self.end = end
        self.pilot_id = pilot_id
        self.desc = desc

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, the_id: uuid.UUID) -> None:
        self._id = the_id

    @property
    def start(self) -> datetime:
        return self._start

    @start.setter
    def start(self, start: datetime) -> None:
        self._start = start

    @property
    def end(self) -> datetime:
        return self._end

    @end.setter
    def end(self, end: datetime) -> None:
        self._end = end

    @property
    def pilot_id(self) -> uuid.UUID:
        return self._pilot_id

    @pilot_id.setter
    def pilot_id(self, pilot_id: uuid.UUID) -> None:
        self._pilot_id = pilot_id

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, desc: str) -> None:
        self._desc = desc
