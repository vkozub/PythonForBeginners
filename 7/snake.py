"""Snake module"""

class Snake:
    """Snake base class"""

    def __init__(self, position, body='+'):
        self._body = body
        self._position = position
        self._head = position
        self._tail = position

    @property
    def position(self):
        """Get snake position"""
        return self._position

    @position.setter
    def position(self, position):
        """Set snake position"""
        self._position = position

    @property
    def head(self):
        """Get snake head position"""
        return self._head

    @head.setter
    def head(self, position):
        """Set snake head position"""
        self._head = position

    @property
    def tail(self):
        """Set snake tail position"""
        return self._tail

    @tail.setter
    def tail(self, position):
        """Set snake tail position"""
        self._tail = position

    @property
    def body(self):
        """Get snake body"""
        return self._body
