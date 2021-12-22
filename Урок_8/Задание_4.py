s = input()
if ord(s)>= 97 and ord(s) <= 122 and s.islower():
  s = s.upper()
elif ord(s)>= 65 and ord(s) <= 90 and s.isupper():
  s = s.lower()
print(s)
