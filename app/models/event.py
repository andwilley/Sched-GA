import uuid
from datetime import datetime

class Event():

    def __init__(self, start: datetime, end: datetime, desc: str, qual_req: str) -> None:
        self.id = uuid.uuid4()
        self.start = start
        self.end = end
        self.desc = desc
        self.qual_req = qual_req

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, the_id: uuid.UUID):
        self._id = the_id

    @property
    def start(self) -> datetime:
        return self._start

    @start.setter
    def start(self, start_time: datetime) -> None:
        self._start = start_time

    @property
    def end(self) -> datetime:
        return self._end

    @end.setter
    def end(self, end: datetime) -> None:
        self._end = end

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, desc: str):
        self._desc = desc

    @property
    def qual_req(self) -> str:
        return self._qual_req

    @qual_req.setter
    def qual_req(self, qual_req: str):
        self._qual_req = qual_req

    def __repr__(self):
        return "eventId {}, start {}, end {}, desc {}, qual {}".format(
            self.id, self.start, self.end, self.desc, self.qual_req)
