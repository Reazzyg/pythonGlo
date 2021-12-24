numbers = []
print('Введите количесвто символов')
ammount_of_numbers = int(input())
for i in range(ammount_of_numbers):
    print('Введите символ')
    numbers.append(input())
for j in range(len(numbers)-1):
    if numbers.count(numbers[j]) == 1:
        print(numbers[j])
