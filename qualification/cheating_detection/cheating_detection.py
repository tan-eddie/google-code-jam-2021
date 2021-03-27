
# Find the cheater (indexed from 1)
def find_cheater(results):
    # Sort questions by hardest difficulty
    num_correct_for_question = []
    for question in range(len(results[0])):
        num_correct = 0
        for user in range(len(results)):
            num_correct += results[user][question]
        num_correct_for_question.append((question, num_correct))

    num_correct_for_question.sort(key=lambda x: x[1])

    # Then take the user that appears the most in 1000 (10%) hardest questions
    counts_by_user = {}
    for i in range(100):
        question = num_correct_for_question[i][0]
        for user in range(len(results)):
            if results[user][question]:
                if user in counts_by_user:
                    counts_by_user[user] += 1
                else:
                    counts_by_user[user] = 1

    cheater = max(counts_by_user, key=counts_by_user.get)
    # Return value is 1-indexed
    return cheater + 1


def main():
    num_cases = int(input())
    # We don't need P
    input()
    for i in range(num_cases):
        results = []
        for j in range(100):
            results.append([int(c) for c in input()])
        print("Case #{:d}: {:d}".format(i+1, find_cheater(results)))


if __name__ == "__main__":
    main()
