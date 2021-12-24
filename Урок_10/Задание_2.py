def multiple(first_store, second_store):
    first_store = first_store.split()
    second_store = second_store.split()
    for i in range(len(first_store)):
        a = int(first_store.pop(i))
        first_store.insert(i, a)
    for i in range(len(second_store)):
        a = int(second_store.pop(i))
        second_store.insert(i, a)
    print(max(first_store) * max(second_store))


first_store = input()
second_store = input()
multiple(first_store, second_store)
