def rank(num1):
    cnt = 0
    while num1 > 0:
        num1 = num1 // 10
        cnt += 1
    return cnt


num1 = int(input())
first_rank = rank(num1)
num1 = int(input())
second_rank = rank(num1)
multiple = first_rank*second_rank
print(multiple)
