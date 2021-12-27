import random


def secret(right_border):
    secret_number = random.randint(1, right_border)
    return secret_number


def count_tries(left_border, right_border):
    while True:
        if left_border > right_border:
            return False
        cnt = 0
        m = left_border+(right_border-left_border)/2
        if i < secret_number:
            i = m+1
            cnt += 1
        elif i > secret_number:
            i = m-1
            cnt += 1
        elif i == secret_number:
            return m, cnt
            break


left_border = int(input())
right_border = int(input())
secret_number = secret(right_border)
print(count_tries(left_border, right_border))
