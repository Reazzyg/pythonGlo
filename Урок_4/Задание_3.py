post1 = input()
post2 = input()
post3 = input()
if len(post1) > len(post2) and len(post1) > len(post3):
    print(post1)
elif len(post2) > len(post3) and len(post2) > len(post1):
    print(post2)
else:
    print(post3)
