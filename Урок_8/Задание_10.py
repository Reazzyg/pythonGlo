s = input()
total = 1
for i in range(len(s)-1):
  if s[i] == chr(32):
    total +=1
print(total)