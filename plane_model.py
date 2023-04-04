from linkedpriorityqueue import LinkedPriorityQueue


class Priority(object):
    """Represents a flyer's priority in boarding."""

    def __init__(self, rank):
        self.rank = rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __str__(self):
        """Returns the string rep of a condition."""
        if self.rank == 1:
            return "Active Military"
        elif self.rank == 2:
            return "Senior Citizen"
        elif self.rank == 3:
            return "Unattended Minor"
        elif self.rank == 4:
            return "Priority Queue Boarding"
        elif self.rank == 5:
            return "First Class"
        elif self.rank == 6:
            return "Business Class"
        elif self.rank == 7:
            return "Economy Class"
        elif self.rank == 8:
            return 'Lowest Priority'


class Flyer(object):
    """Represents a flyer with a name and priority."""

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __str__(self):
        """Returns the string rep of a patient."""
        return self.name + " / " + str(self.priority)


class PlaneModel(object):
    """Model of a scheduler."""

    def __init__(self):
        self.boarding_queue = LinkedPriorityQueue()

    def isEmpty(self):
        """Returns False if there are patients in the model
        or True otherwise."""
        return len(self.boarding_queue) == 0

    def schedule_flyer(self, flyer):
        """Adds a patient to the schedule."""
        self.boarding_queue.add(flyer)

    def board_flyer(self):
        """Returns the patient treated or None if there are none."""
        return self.boarding_queue.pop()
