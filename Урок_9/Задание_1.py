search_count = int(input())
storage = []
for i in range(search_count):
    storage.append(input())
search = input()
for i in range(search_count):
    lower_case = storage[i].lower()
    if lower_case.find(search.lower()) != -1:
        print(storage[i])
