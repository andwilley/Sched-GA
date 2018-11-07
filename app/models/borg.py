from typing import Any

class Borg:
    __shared_state: Any = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return self.__shared_state
