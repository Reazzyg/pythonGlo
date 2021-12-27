def take_max(store):
    store = store.split()
    for i in range(len(store)):
        a = int(store.pop(i))
        store.insert(i, a)
    return max(store)


first_store = input()
first_max = take_max(first_store)
second_store = input()
second_max = take_max(second_store)
multiple = first_max*second_max
print(multiple)
