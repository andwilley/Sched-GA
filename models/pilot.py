import uuid

class Pilot():

    def __init__(self) -> None:
        self.id = uuid.uuid4()

    @property
    def id(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return "pilotId {}".format(self.id)
