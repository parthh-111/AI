from collections import deque

class EightPuzzle:
    def __init__(self, start, goal):
        self.start = tuple(start)
        self.goal = tuple(goal)

    def get_neighbors(self, state):
        neighbors = []

        blank = state.index(0)
        row = blank // 3
        col = blank % 3

        moves = [
            (-3, "Up"),
            (3, "Down"),
            (-1, "Left"),
            (1, "Right")
        ]

        for change, direction in moves:
            if direction == "Up" and row == 0:
                continue
            if direction == "Down" and row == 2:
                continue
            if direction == "Left" and col == 0:
                continue
            if direction == "Right" and col == 2:
                continue

            new = blank + change
            new_state = list(state)

            new_state[blank], new_state[new] = new_state[new], new_state[blank]

            neighbors.append((tuple(new_state), direction))

        return neighbors

    def bfs(self):
        queue = deque([(self.start, [("Start", self.start)])])
        visited = {self.start}

        while queue:
            state, path = queue.popleft()

            if state == self.goal:
                return path

            for next_state, move in self.get_neighbors(state):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, path + [(move, next_state)]))

        return None

    def print_board(self, state):
        for i in range(0, 9, 3):
            print(state[i], state[i + 1], state[i + 2])
        print()


# Initial and Goal States
start = (
    1, 2, 3,
    4, 0, 5,
    7, 8, 6
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

puzzle = EightPuzzle(start, goal)
solution = puzzle.bfs()

if solution:
    print("Initial State to Goal State:\n")

    for step, (move, state) in enumerate(solution):
        print(f"Step {step}")
        print("Move:", move)
        puzzle.print_board(state)

    print("Goal State Reached!")
    print("Total Moves:", len(solution) - 1)
else:
    print("No solution found.")
