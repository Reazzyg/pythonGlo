num = input()
num_storage = num.split()
a = 0
for i in range(len(num_storage) - 1):
    a += num_storage.count(num_storage[i])
print(a)
