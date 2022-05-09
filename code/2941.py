c_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in c_word:
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))