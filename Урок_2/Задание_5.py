ammount = int(input())
hour = int(ammount/3600)
middle = ammount - 3600*hour
minute = int(middle/60)
sec = int(middle - minute*60)
print(ammount, 'секунд - это', hour, 'час', minute, 'минут', sec, 'секунд')
