a = input()
b = input()
if ord(a)<ord(b):
  for i in range(ord(a),ord(b)+1):
    print(chr(i))
else:
  for i in range(ord(b),ord(a)+1):
    print(chr(i))