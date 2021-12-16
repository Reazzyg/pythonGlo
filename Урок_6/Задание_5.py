num = int(input())
cnt_positive = 0
cnt_negative = 0
while num != 0:
    if num < 0:
        cnt_negative += 1
    else:
        cnt_positive += 1
    print(cnt_positive)
    print(cnt_negative)
    num = int(input())
print(cnt_positive*cnt_negative)
