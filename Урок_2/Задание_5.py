ammount = int(input())
hour = ammount//3600
middle = ammount - 3600*hour
minute = middle//60
sec = middle - minute*60
print(ammount, 'секунд - это', hour, 'час', minute, 'минут', sec, 'секунд')
