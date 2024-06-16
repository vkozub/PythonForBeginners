"""Snake module"""

class Snake:
    """Snake base class"""

    def __init__(self, position, body='+'):
        self._body = body
        self._position = position

    @property
    def position(self):
        """Get snake position"""
        return self._position

    @position.setter
    def position(self, position):
        """Set snake position"""
        self._position = position

    @property
    def body(self):
        """Get snake body"""
        return self._body
