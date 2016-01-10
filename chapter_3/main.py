from chapter_3.utils import Solution, State
from chapter_3.problems import Deterministic
from chapter_3.solvers import BreadthFirstSearch, DepthLimitedSearch, DepthFirstSearch

from collections import namedtuple
import numpy as np

if __name__ == '__main__':
    WorldSize = namedtuple('WorldSize', ['x', 'y'])

    # status = np.matrix([['clean', 'dirty', 'dirty', 'clean', 'dirty'],
    #          ['clean', 'dirty', 'dirty', 'clean', 'dirty'],
    #          ['clean', 'dirty', 'dirty', 'clean', 'dirty'],
    #          ['clean', 'dirty', 'dirty', 'clean', 'dirty'],
    #          ['clean', 'dirty', 'dirty', 'clean', 'dirty']])

    status = np.matrix([['dirty'] * 3] * 3)

    world_size = WorldSize(3, 3)
    initial_state = State(status=status, x=0, y=0)

    solution = Solution()
    problem = Deterministic(initial_state=initial_state, size=world_size, solution=solution)
    solver = BreadthFirstSearch()
    # solver = DepthLimitedSearch(10)
    # solver = DepthFirstSearch()
    solver.execute(problem)
    print(problem.solution.actions)
