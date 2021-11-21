translater = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
result = []
with open("text_HW4_output.txt", "r") as file_obj:
    for line in file_obj:
        lst = line.split()
        lst[2] = translater.get(lst[0])
        result.append(''.join(lst) + '\n')
with open("text_HW4_input.txt", "w+") as file_input:
    file_input.writelines(result)
    file_input.seek(0)
    print(file_input.read())
