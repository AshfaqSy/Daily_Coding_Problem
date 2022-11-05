"""There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

"""


def get_step_combos(num_steps, step_sizes):
    combos = list()

    if num_steps < min(step_sizes):
        return combos

    for step_size in step_sizes:
        if num_steps == step_size:
            combos.append([step_size])
        elif num_steps > step_size:
            child_combos = get_step_combos(num_steps - step_size, step_sizes)
            for child_combo in child_combos:
                combos.append([step_size] + child_combo)
    return combos


assert get_step_combos(4, [1, 2]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
assert get_step_combos(4, [1, 2, 3]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]
