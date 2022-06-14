x = input('Please Input your name:')

uni_list = []

for letter in x:
    uni_list.append(str(ord(letter)))
    
print(' | '.join(uni_list))