
# Reverse sublist of l from index i to j (inclusive)
def reverse_sublist(l, i, j):
    num_swaps = (j - i + 1) // 2
    for s in range(num_swaps):
        l[i + s], l[j - s] = l[j - s], l[i + s]

def list_for_cost(n, c):
    # Min cost for n is (n-1) (1+1+1+... up to second last element).
    # Max cost for n is n+(n-1)+(n-2)+...+2 = (n-1)/2 * (n + 2) (arithmetic sum)
    if c < n-1 or c > (n-1)*(n+2)/2:
        return "IMPOSSIBLE"

    l = list(range(1, n+1))
    level = 0
    start_offset = 0
    end_offset = 0
    remaining_cost = c - n + 1 # Subtract the min 1 cost at each level
    while remaining_cost:
        max_additional_cost_at_level = n - level - 1
        if remaining_cost >= max_additional_cost_at_level:
            reverse_sublist(l, start_offset, n - 1 - end_offset)
            
            if level % 2 == 0:
                # Even level, so increment end offset
                end_offset += 1
            else:
                # Odd level, so increment start offset
                start_offset += 1

            level += 1
            remaining_cost -= max_additional_cost_at_level
        else:
            if level % 2 == 0:
                # Even level, so apply offset from start_offset
                reverse_sublist(l, start_offset, start_offset + remaining_cost)
            else:
                # Odd level, so apply offset from end_offset
                reverse_sublist(l, n - 1 - end_offset - remaining_cost, n - 1 - end_offset)

            remaining_cost = 0

    return " ".join(map(str, l))

def main():
    num_cases = int(input())
    for i in range(num_cases):
        case = input().split()
        n = int(case[0])
        c = int(case[1])
        print("Case #{:d}: {:s}".format(i+1, list_for_cost(n, c)))

if __name__ == "__main__":
    main()
