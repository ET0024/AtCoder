import string


def print_query(lst, x, y):
    print('?', lst[x], lst[y])


def get_answer_and_swap(lst, x, y):
    # x, y is compared index for lst that satisfies y > x

    print_query(lst, x, y)
    ans = input()

    if ans == '>':
        lst[x], lst[y] = lst[y], lst[x]

    return lst


n, q = map(int, input().split())
letters = list(string.ascii_letters[26:26 + n])

for i in range(n - 1):
    for j in range(n - i - 1):
        letters = get_answer_and_swap(letters, j, j + 1)
        print(letters)

print("!", "".join(letters))
