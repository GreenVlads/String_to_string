from dictionary import symbols

file_out = open('out.txt', 'w')
count_of_lines = 7    # количество строк 

print('Пожалуйста, вводите только символы из этого списка:' + '(' + ''.join(symbols.keys()) + ')' )
print('Введите строку:\n')

input_string = input()
input_string = input_string.lower()    # приведение строки к нижнему регистру

for string in range(count_of_lines):    # построчный вывод
    for char in input_string:
        if char in symbols.keys():
            for elem in symbols[char][string]:
                if elem == '':
                    file_out.write(' ')
                else:
                   file_out.write(char.upper())
            file_out.write(' ')
        else:
            continue
    file_out.write('\n')
