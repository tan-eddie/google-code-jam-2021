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


# Inserts i in list l by querying in a bisecting manner.
def bisection_insert(i, l, start, end):
    mid = ((end - start) >> 1) + start
    m = query_median(i, l[mid], l[mid+1])
    if m == i:
        l.insert(mid+1, i)
    elif m == l[mid]:
        # i belongs in starting half
        if mid-1 < start:
            l.insert(start, i)
        else:
            bisection_insert(i, l, start, mid)
    else:
        # i belongs in ending half
        if mid+1 >= end:
            l.insert(end+1, i)
        else:
            bisection_insert(i, l, mid, end)


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

    # Run insertion algorithm with bisect queries
    # Note: this passed test sets 1 and 2 but I don't think it'll
    # pass 3 because max number of queries needed for that set is
    # 1 + ceil(log2(4)) + ceil(log2(5)) + ... + ceil(log2(50))
    # = 235
    # which is >170 per test case in test set 3.
    for i in range(4, n+1):
        bisection_insert(i, l, 0, len(l)-1)

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
