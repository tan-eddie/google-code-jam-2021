
# Min cost of a subpattern of ??? optionally bounded on each end by C|J.
def min_cost_subpattern(x, y, subpattern):
    if len(subpattern) < 2:
        return 0

    if subpattern == "CJ":
        return x
    elif subpattern == "JC":
        return y
    elif subpattern == "CC" or subpattern == "JJ":
        return 0

    # Remaining cases all have at least one ?
    # Follow cases described here: https://docs.google.com/spreadsheets/d/1LpUPprPPPNsvW59g49r7wdZwmA4FhobjF2TggKjzO64/edit?usp=sharing
    start = subpattern[0]
    end = subpattern[-1]
    num_choices = len(subpattern)
    if start != "?":
        num_choices -= 1
    if end != "?":
        num_choices -= 1
    is_even = num_choices % 2 == 0

    min_alt_cost = (num_choices // 2) * (x + y)

    if start == "?" and end == "?":
        min_const_cost = 0
        if is_even:
            min_alt_cost += min(-x, -y)

    elif (start == "?" and end == "C") or (start == "J" and end == "?"):
        min_const_cost = min(0, y)
        if is_even:
            min_alt_cost += min(0, -x)
        else:
            min_alt_cost += min(0, y)

    elif (start == "?" and end == "J") or (start == "C" and end == "?"):
        min_const_cost = min(0, x)
        if is_even:
            min_alt_cost += min(0, -y)
        else:
            min_alt_cost += min(0, x)

    elif start == end:
        min_const_cost = min(0, x+y)
        if not is_even:
            min_alt_cost += min(0, x+y)

    elif start == "C" and end == "J":
        min_const_cost = x
        if is_even:
            min_alt_cost += min(x, -y)
        else:
            min_alt_cost += x

    elif start == "J" and end == "C":
        min_const_cost = y
        if is_even:
            min_alt_cost += min(-x, y)
        else:
            min_alt_cost += y

    return min(min_alt_cost, min_const_cost)

def min_cost(x, y, pattern):
    cost = 0
    # Sum cost of each subpattern
    start = 0
    for i in range(len(pattern)):
        if pattern[i] != "?":
            cost += min_cost_subpattern(x, y, pattern[start:i+1])
            start = i

    # Handle the case where last char is ?
    cost += min_cost_subpattern(x, y, pattern[start:len(pattern)])
    return cost

def main():
    num_cases = int(input())
    for i in range(num_cases):
        case = input().split()
        x = int(case[0]) # cost of CJ
        y = int(case[1]) # cost of JC
        pattern = case[2]
        print("Case #{:d}: {:d}".format(i+1, min_cost(x, y, pattern)))

if __name__ == "__main__":
    main()
