"""
Sniv Model.
"""

import uuid
from datetime import datetime

class Sniv:
    """
    Represents a single schedule request, or "sniv".
    """

    def __init__(self, start: datetime, end: datetime, pilot_id: uuid.UUID, desc: str = ''):
        """
        Creates a Sniv.

        Args:
            start: the start time and date
            end: the end time and date
            pilot_id: the ID of the pilot this sniv is associated with
            desc: a brief plain-language description of this sniv
        """

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
