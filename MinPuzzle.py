# Name: Joshua Jansen
# OSU Email: Jansejos@oregonstate.edu
# Course: CS325
# Assignment: 7

def minEffort(puzzle):
    rows = len(puzzle)
    cols = len(puzzle[0])

    effort = [[float('infinity')] * cols for _ in range(rows)]
    effort[0][0] = 0

    queue = [(0, 0, 0)]
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while len(queue) > 0:
        curr_row, curr_col, cur_effort = queue.pop(0)
        if cur_effort >= effort[curr_row][curr_col]:
            for i, j in neighbors:
                if 0 <= curr_row + i < rows and 0 <= curr_col + j < cols:
                    new_effort = max(cur_effort, abs(puzzle[curr_row][curr_col] - puzzle[curr_row + i][curr_col + j]))
                    if new_effort < effort[curr_row + i][curr_col + j]:
                        queue.append((curr_row + i, curr_col + j, new_effort))
                        effort[curr_row + i][curr_col + j] = new_effort
    return effort[rows - 1][cols - 1]

