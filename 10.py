# http://www.pythonchallenge.com/pc/return/bull.html

current_num = '1'
for i in range(30):

    tmp_char = ''
    tmp_count = 0
    next_num = ''
    for char in current_num:
        if char == tmp_char:
            tmp_count += 1
        else:
            if tmp_count != 0:
                next_num += '{}{}'.format(tmp_count, tmp_char)
            tmp_char = char
            tmp_count = 1
    next_num += '{}{}'.format(tmp_count, tmp_char)
    current_num = next_num

    print(current_num)
    print(len(current_num))
