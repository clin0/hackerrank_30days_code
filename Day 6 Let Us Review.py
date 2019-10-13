### METHOD 1, FOR loop

#input number of cases you want to seperate
number_of_case = int(input())

#input the case content
for i in range(number_of_case):
    case_content = input()

    even_index_char = ''
    odd_index_Char = ''

    for j in range(len(case_content)):
        if j % 2 == 0:
            even_index_char += case_content[j]
        else:
            odd_index_Char += case_content[j]

    print(even_index_char + ' ' + odd_index_Char)




'''
### METHOD 2, Python slice build-in YES I LIKE IT ;)

#input number of cases you want to seperate
number_of_case = int(input())

#input the case content
for i in range(number_of_case):
    case_content = input()
    
    even_index_char = case_content[::2]
    odd_index_Char = case_content[1::2]

print('{} {}'.format(even_index_char, odd_index_Char))
'''