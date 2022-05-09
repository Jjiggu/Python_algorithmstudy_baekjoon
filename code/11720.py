import string

a = input()
for i in string.ascii_lowercase:
    print(a.find(i), end = " ")