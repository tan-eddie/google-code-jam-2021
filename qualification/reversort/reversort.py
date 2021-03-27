
# Reverse sublist of l from index i to j (inclusive)
def reverse_sublist(l, i, j):
    num_swaps = (j - i + 1) // 2
    for s in range(num_swaps):
        l[i + s], l[j - s] = l[j - s], l[i + s]

def cost(n, l):
    c = 0
    for i in range(n - 1):
        # find j
        for j in range(i, n):
            if l[j] == i + 1:
                break

        c += j - i + 1
        reverse_sublist(l, i, j)

    return c

def main():
    num_cases = int(input())
    for i in range(num_cases):
        n = int(input())
        l = [int(x) for x in input().split()]
        print("Case #{:d}: {:d}".format(i+1, cost(n, l)))

if __name__ == "__main__":
    main()
