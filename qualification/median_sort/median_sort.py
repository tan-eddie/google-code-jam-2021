import sys


# 1 <= i, j, k <= n where n is number of elements to sort
# Returns the median, or -1 if query quota exceeded
def query_median(i, j, k):
    print("{:d} {:d} {:d}".format(i, j, k))
    sys.stdout.flush()
    median = int(input())
    if median == -1:
        exit()
    return median


# Inserts i in list l using ternary search (split into 3 buckets)
def ternary_insert(i, l, start, end):
    # Split [start, end] interval into [start, a, b, end] and
    # recursively call ternary insert in each subinterval
    # [start, a], [a, b] and [b, end].
    interval = (end - start) // 3

    if interval == 0:
        # end - start < 3 (i.e <=3 elements in [start, end])
        a = start
        b = start + 1
    else:
        a = start + interval
        b = a + interval
    median = query_median(i, l[a], l[b])
    if median == i:
        # i belongs in [a, b]
        if (a+1) >= b:
            l.insert(b, i)
        else:
            ternary_insert(i, l, a, b)
    elif median == l[a]:
        # i belongs in [start, a]
        if a-1 < start:
            l.insert(start, i)
        else:
            ternary_insert(i, l, start, a)
    elif median == l[b]:
        # i belongs in [b, end]
        if b+1 > end:
            l.insert(end+1, i)
        else:
            ternary_insert(i, l, b, end)


# n: number of elements to sort
def process_test_case(n):
    # Initial query and setup
    m = query_median(1, 2, 3)
    if m == 1:
        l = [2, 1, 3]
    elif m == 2:
        l = [1, 2, 3]
    else:
        l = [1, 3, 2]

    # Run insertion sort with ternary search.
    # Note: It should pass all test sets because max number of
    # queries needed for n = 50 is:
    # 1 + ceil(log3(4)) + ceil(log3(5)) + ... + ceil(log3(50))
    # = 159
    # which is <170 per test case in test set 3.
    for i in range(4, n+1):
        ternary_insert(i, l, 0, len(l)-1)

    print(" ".join(map(str, l)))
    sys.stdout.flush()
    result = int(input())
    return result


def main():
    num_cases, n, q = tuple(int(x) for x in input().split())
    for i in range(num_cases):
        result = process_test_case(n)
        if result == -1:
            exit()


if __name__ == "__main__":
    main()
