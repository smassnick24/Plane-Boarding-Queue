# Source https://stackoverflow.com/questions/42317990/proper-use-of-inheritance-in-tkinter-using-button-widget

from tkinter import Button


class PlaneButton(Button):
    """ A child class of the Tkinter Button class.
        This is used to store extra information about the plane
        for the SQL database."""
    def __init__(self, parent, seat_class, seat_id, *args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.seat_id = seat_id
        self.seat_class = seat_class
