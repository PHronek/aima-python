from chapter_3.utils import Node


class BreadthFirstSearch:
    def __init__(self):
        self.frontier = []
        self.explored = []

    def execute(self, problem):
        node = Node(state=problem.initial_state, action=None, parent=None)
        self.frontier.append(node)
        if problem.goal_test(node.state):
            return problem.solution.create(node)
        while True:
            if len(self.frontier) == 0:
                return 'Failure'
            node = self.frontier.pop()
            self.explored.append(node)
            for action in problem.actions(node.state):
                next_state = problem.generate_state(node.state, action)
                child = Node(state=next_state, action=action, parent=node)
                if not((child in self.frontier) or (child in self.explored)):
                    if problem.goal_test(child.state):
                        return problem.solution.create(child)
                    self.frontier.append(child)


class DepthFirstSearch:
    def __init__(self):
        self.frontier = []
        self.explored = []

    def execute(self, problem):
        node = Node(state=problem.initial_state, action=None, parent=None)
        self.frontier.append(node)
        if problem.goal_test(node.state):
            return problem.solution.create(node)
        while True:
            if len(self.frontier) == 0:
                return 'Failure'
            node = self.frontier.pop(0)
            self.explored.append(node)
            for action in problem.actions(node.state):
                next_state = problem.generate_state(node.state, action)
                child = Node(state=next_state, action=action, parent=node)
                if not((child in self.frontier) or (child in self.explored)):
                    if problem.goal_test(child.state):
                        return problem.solution.create(child)
                    self.frontier.append(child)


class DepthLimitedSearch:
    def __init__(self, limit):
        self.limit = limit

    def execute(self, problem):
        return self.recursive_dls(Node(state=problem.initial_state, action=None, parent=None), problem, self.limit)

    def recursive_dls(self, node, problem, limit):
        if problem.goal_test(node.state):
            return problem.solution.create(node)
        if limit == 0:
            print('cutoff')
            return 'cutoff'
        else:
            cutoff_occured = False
            for action in problem.actions(node.state):
                next_state = problem.generate_state(node.state, action)
                child = Node(state=next_state, action=action, parent=node)
                result = self.recursive_dls(child, problem, limit - 1)
                if result == 'cutoff':
                    cutoff_occured = True
                if result != 'failure':
                    return result
            if cutoff_occured:
                print('cutoff')
                return 'cutoff'
            else:
                print('failure')
                return 'failure'

