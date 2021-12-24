def multiple(num1, num2):
    cnt1 = 0
    cnt2 = 0
    while num1 > 0:
        num1 = num1 // 10
        cnt1 += 1

    while num2 > 0:
        num2 = num2 // 10
        cnt2 += 1
    return cnt1*cnt2


num1 = int(input())
num2 = int(input())
print(multiple(num1, num2))
