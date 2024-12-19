def sum_of_one_to(n: int) -> int:
    result = 0
    while n > 0:
        result += n
        n -= 1
    return result


def recursive_sum_of_one_to(n: int) -> int:
    if n > 1: # No recursive call with 0
        return n + recursive_sum_of_one_to(n - 1)
    return n

NUMBER = 5
print("Normal:    ", sum_of_one_to(NUMBER))
print("Recursive: ", recursive_sum_of_one_to(NUMBER))


def faculty(n: int):
    if n <= 1:
        return 1
    if n > 1: # No recursive call with 0
        return n * recursive_sum_of_one_to(n - 1)

print(faculty(0))
print(faculty(1))
print(faculty(2))
print(faculty(3))
