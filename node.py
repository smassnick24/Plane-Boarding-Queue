"""
File: node.py
"""


class Node(object):
    """Nodes for singly linked structures."""

    def __init__(self, data, next=None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)