# Name: Joshua Jansen
# OSU Email: Jansejos@oregonstate.edu
# Course: CS325
# Assignment: 7

def minEffort(puzzle):
    rows = len(puzzle)
    cols = len(puzzle[0])
    queue = [(0, 0, 0)]
    effort = None
    neighbors = [(0, 1), (1, 0)]
    while len(queue) > 0:
        curr_row, curr_col, cur_effort = queue.pop(0)
        if curr_row == rows - 1 and curr_col == cols - 1:
            if effort is None:
                effort = cur_effort
            else:
                min(cur_effort, effort)
        for i, j in neighbors:
            if curr_row + i < rows and curr_col + j < cols:
                queue.append((curr_row + i, curr_col + j, max(cur_effort, abs(puzzle[curr_row][curr_col] -
                                                                              puzzle[curr_row + i][curr_col + j]))))
    return effort
