"""
EventGene class definition.
"""

import uuid

class EventGene():
    """
    Map an event ID to a pilot ID.
    """

    def __init__(self, event_id: uuid.UUID) -> None:
        """
        Create the EventGene

        Args:
            event_id: the ID of the event associated with this gene.

        Returns:
            None
        """

        self.event_id = event_id
        self.pilot_id = None

    @property
    def event_id(self) -> uuid.UUID:
        """
        The event ID of the event associated with this gene.
        """

        return self._event_id

    @event_id.setter
    def event_id(self, event_id: uuid.UUID):
        self._event_id = event_id

    @property
    def pilot_id(self) -> uuid.UUID:
        """
        The pilot ID of the event associated with this gene.
        """

        return self._pilot_id

    @pilot_id.setter
    def pilot_id(self, pilot_id: uuid.UUID):
        self._pilot_id = pilot_id

    def copy(self) -> 'EventGene':
        """
        Create a copy of the gene.

        Returns:
            A new EventGene object with fields set to the same IDs.
        """

        gene = EventGene(self.event_id)
        gene.pilot_id = self.pilot_id
        return gene

    def __repr__(self):
        return "event_id {}, pilot_id {}".format(self.event_id, self.pilot_id)
