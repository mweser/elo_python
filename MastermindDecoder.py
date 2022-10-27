# Types of values: hits, nicks, and misses

def constraint_4(sol):
    seq_arr = seq_to_arr(sol)
    return sum_values(seq_arr) == seq_arr[3] * 10 + seq_arr[4]


def sum_values(seq_arr):
    sum = 0
    for value in seq_arr:
        sum += int(value)
    return sum


def constraint_3(seq, sol, hits=2, nicks=0):
    pass


def constraint_2(seq, sol, hits=1, nicks=1):
    pass


def assert_constraint(seq, sol, hits, nicks):
    seq_arr = seq_to_arr(seq)
    sol_arr = seq_to_arr(sol)

    hit_count, nick_count = count_hits(seq_arr, sol_arr)

    return hits == hit_count and nicks == nick_count


def constraint_1(seq, sol, hits=0, nicks=1):
    return assert_constraint(seq, sol, hits, nicks)


def count_hits(arr1, arr2):
    hit_count = 0
    nick_count = 0
    size = min(len(arr1), len(arr2))

    for i in range(0, size):
        if arr1[i] == arr2[i]:
            hit_count += 1
        else:
            pass
    return hit_count, nick_count


def seq_to_arr(seq):
    arr = []
    for char in str(seq):
        arr.append(int(char))
    # print(arr)
    return arr


solution = 57628

sequence = 12345
seq_arr = seq_to_arr(sequence)

sequence = 79314
print(f'Constraint 1: {constraint_1(sequence, solution)}')

sequence = 95643
print(f'Constraint 2: {constraint_2(sequence, solution)}')

sequence = 57319
print(f'Constraint 3: {constraint_3(sequence, solution)}')

print(f'Constraint 4: {constraint_4(solution)} \t\t\t(A + B + C + D + E = D * 10 + E)')
