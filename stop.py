"""
    Name: Stop Class
    File: stop.py
    Version: 1
    Description: Common stop class for inheritance
    Each stop must implement these methods
"""


class Stop:
    def __init__(self, name):
        self.name = name

    def get_description(self):
        pass

    def interact(self, player):
        pass
