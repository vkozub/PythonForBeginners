"""Apple module"""

class Apple:
    """Apple base class"""

    def __init__(self, position, body='@'):
        self._body = body
        self._position = position

    @property
    def position(self):
        """Get apple position"""
        return self._position

    @position.setter
    def position(self, position):
        """Set apple position"""
        self._position = position

    @property
    def body(self):
        """Get apple body"""
        return self._body
