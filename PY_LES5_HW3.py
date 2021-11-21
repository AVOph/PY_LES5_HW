firm = {'Иванов': 25, 'Пупкин': 10, 'Петров': 15, 'Путин': 50}
with open("text_HW3.txt", "w") as file_obj:
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
summa = 0
count = 0
persons = []
with open("text_HW3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Сотрудники с окладом менее 20к: {persons}")
print(f"Средняя величина дохода: {result}")
