"""Snake module"""

class Snake:
    """Snake base class"""

    def __init__(self, position, body='+'):
        self._body = body
        self._position = position
        self._previous_position = None

    @property
    def position(self):
        """Get snake position"""
        return self._position

    @position.setter
    def position(self, position):
        """Set snake position"""
        self._previous_position = self._position
        self._position = position

    @property
    def previous_position(self):
        """Get apple previous position"""
        return self._previous_position

    @property
    def body(self):
        """Get snake body"""
        return self._body
