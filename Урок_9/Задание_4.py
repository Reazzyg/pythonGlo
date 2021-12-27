num = input()
num_storage = num.split()
repeat_count = []
for n in num_storage:
    repeat_count.append(num_storage.count(n)-1)
print(int(sum(repeat_count)/2))
