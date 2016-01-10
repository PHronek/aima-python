class State:
    def __init__(self, status, x, y):
        self.status = status
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.status.tolist() == other.status.tolist() and self.x == other.x and self.y == other.y

    def __repr__(self):
        return '<%s %s %s %s>' % (self.__class__.__name__, self.x, self.y, self.status)


class Node:
    def __init__(self, state, action=None, parent=None):
        self.state = state
        self.action = action
        self.parent = parent

    def __eq__(self, other):
        return self.state == other.state

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.state)


class Solution:
    def __init__(self):
        self.actions = []

    def create(self, node):
        if not node.parent:
            return self.actions.reverse()
        else:
            self.actions.append(node.action)
            self.create(node.parent)
