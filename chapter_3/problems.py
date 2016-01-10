from chapter_3.utils import State
import numpy as np


class Deterministic:
    def __init__(self, initial_state, size, solution):
        self.initial_state = initial_state
        self.size_x = size.x
        self.size_y = size.y
        self.solution = solution

    def actions(self, state):
        if state.x == 0 and state.y == 0:
            return ['down', 'right', 'suck']
        if state.x == self.size_x - 1 and state.y == 0:
            return ['up', 'right', 'suck']
        if state.x == 0 and state.y == self.size_y - 1:
            return ['down', 'left', 'suck']
        if state.x == self.size_x - 1 and state.y == self.size_y - 1:
            return ['up', 'left', 'suck']
        if state.x == 0:
            return ['down', 'left', 'right', 'suck']
        if state.x == self.size_x:
            return ['up', 'left', 'right', 'suck']
        if state.y == 0:
            return ['up', 'down', 'right', 'suck']
        if state.y == self.size_y - 1:
            return ['up', 'down', 'left', 'suck']
        else:
            return ['up', 'down', 'left', 'right', 'suck']

    def goal_test(self, state):
        dirty_count = state.status.getA().flatten().tolist().count('dirty')
        print(dirty_count)
        return dirty_count == 0

    def generate_state(self, previous_state, action):
        if action == 'up':
            if previous_state.x == 0:
                return State(previous_state.status, previous_state.x, previous_state.y)
            else:
                return State(previous_state.status, previous_state.x - 1, previous_state.y)
        if action == 'down':
            if previous_state.x == self.size_x - 1:
                return State(previous_state.status, previous_state.x, previous_state.y)
            else:
                return State(previous_state.status, previous_state.x + 1, previous_state.y)
        if action == 'left':
            if previous_state.y == 0:
                return State(previous_state.status, previous_state.x, previous_state.y)
            else:
                return State(previous_state.status, previous_state.x, previous_state.y - 1)
        if action == 'right':
            if previous_state.y == self.size_y - 1:
                return State(previous_state.status, previous_state.x, previous_state.y)
            else:
                return State(previous_state.status, previous_state.x, previous_state.y + 1)
        if action == 'suck':
            return State(self.generate_status(previous_state.status, previous_state.x, previous_state.y), previous_state.x, previous_state.y)

    def generate_status(self, status, x, y):
        new_matrix = np.matrix(status)
        new_matrix[x, y] = 'clean'
        return new_matrix


