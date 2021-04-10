
def solve_naive_recursive(state, m):
    # m is index in state that we are processing
    if m == len(state):
        sum = 0
        product = 1
        for i in range(len(state)):
            num_in_sum = state[i][2]
            num_in_product = state[i][1] - num_in_sum
            sum += state[i][0] * num_in_sum
            product *= state[i][0] ** num_in_product
        if sum == product:
            return sum
        else:
            return 0

    # Recurse
    max_score = 0
    for i in range(state[m][1] + 1):
        state[m][2] = i
        score = solve_naive_recursive(state, m + 1)
        if score > max_score:
            max_score = score
    return max_score


def solve(state):
    return solve_naive_recursive(state, 0)


def main():
    num_cases = int(input())
    for i in range(num_cases):
        m = int(input())
        state = []
        for j in range(m):
            prime = [int(x) for x in input().split()]
            prime.append(0)
            # State is list of [Pi, Ni, num_in_sum]
            state.append(prime)
        print("Case #{:d}: {:d}".format(i+1, solve(state)))


if __name__ == "__main__":
    main()
