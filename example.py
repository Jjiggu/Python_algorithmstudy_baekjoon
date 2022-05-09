li = 'c= c- dz= d- lj nj s= z='.split(' ')
in_text = input()

i = 0
count = 0
while i < len(li):
    if li[i] in in_text:
        k = in_text.split(li[i])
        count += len(k)-1
        print(k)
        in_text = ''
        for i in range(len(k)):
            in_text += '_'+k[i]
        print(in_text)
    else:
        i += 1
for i in in_text:
    if i != '_':
        count += 1
print(count)