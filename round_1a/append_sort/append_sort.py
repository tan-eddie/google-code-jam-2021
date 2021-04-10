
def solve(n, l):
    operations = 0
    prev = l[0]
    for i in range(1, len(l)):
        curr = l[i]
        max_append_value = 1
        while curr <= prev:
            curr *= 10
            max_append_value *= 10
            operations += 1
            diff = prev - curr
            if diff >= 0 and diff + 1 < max_append_value:
                # Append diff + 1
                curr += diff + 1

        prev = curr
    return operations


def main():
    num_cases = int(input())
    for i in range(num_cases):
        n = int(input())
        l = [int(x) for x in input().split()]
        print("Case #{:d}: {:d}".format(i+1, solve(n, l)))


if __name__ == "__main__":
    main()
