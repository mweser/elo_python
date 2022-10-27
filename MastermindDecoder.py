# Types of values: hits, nicks, and misses

verbose = False
line_break = "\n======================\n"
solutions_arr = []

solution = 57628


def constraint_4(sol):
    if verbose: print("Constraint 4\n")
    seq_arr = seq_to_arr(sol)
    return sum_values(seq_arr) == seq_arr[3] * 10 + seq_arr[4]


def sum_values(seq_arr):
    sum = 0
    for value in seq_arr:
        sum += int(value)
    return sum


def constraint_3(sol, hits=2, nicks=0):
    if verbose: print("Constraint 3\n")
    return assert_constraint(57319, sol, hits, nicks)


def constraint_2(sol, hits=1, nicks=1):
    if verbose: print("Constraint 2\n")
    return assert_constraint(95643, sol, hits, nicks)


def assert_constraint(seq, sol, hits, nicks):
    seq_arr = seq_to_arr(seq)
    sol_arr = seq_to_arr(sol)

    hit_count, nick_count = count_hits(seq_arr, sol_arr)

    return hits == hit_count and nicks == nick_count


def constraint_1(sol, hits=0, nicks=1):
    if verbose: print("Constraint 1\n")
    return assert_constraint(79314, sol, hits, nicks)


def count_hits(arr1, arr2):
    hit_count = 0
    nick_count = 0
    size = min(len(arr1), len(arr2))

    for i in range(0, size):
        if arr1[i] == arr2[i]:
            if verbose: print(
                f'  Found hit:\n  seq[{i}] -> {arr1[i]}\n\tseq: {arr1}\n\tsol: {arr2} \n')
            hit_count += 1
        else:
            for j in range(0, size):
                if arr1[i] == arr2[j] and i != j:
                    if verbose: print(
                        f'  Found nick:\n  seq[{i}] & sol[{j}] -> {arr1[i]}\n\tseq: {arr1}\n\tsol: {arr2} \n')

                    nick_count += 1
    return hit_count, nick_count


def seq_to_arr(seq):
    arr = []
    for char in str(seq):
        arr.append(int(char))
    # print(arr)
    return arr


def sample_check():
    if verbose: print(f'Result: {constraint_1(solution)}{line_break}')
    if verbose: print(f'Result: {constraint_2(solution)}{line_break}')
    if verbose: print(f'Result: {constraint_3(solution)}{line_break}')

    if verbose: print(
        f'Result: {constraint_4(solution)} \t\t\t(A + B + C + D + E = D * 10 + E){line_break}')


def check_constraints(attempt):
    if not constraint_1(attempt):
        if verbose: print(f'{attempt} Failed at Constraint 1\n')
        return

    if not constraint_2(attempt):
        if verbose:   print(f'{attempt} Failed at Constraint 2\n')
        return

    if not constraint_3(attempt):
        if verbose:  print(f'{attempt} Failed at Constraint 3\n')
        return

    if not constraint_4(attempt):
        if verbose: print(f'{attempt} Failed at Constraint 4\n')
        return

    if verbose: print(f'{attempt} Passed all constraints! ')
    solutions_arr.append(attempt)
    return True


for solution in range(10000, 100000):
    check_constraints(solution)

print(f'Solutions:\n{solutions_arr}')
