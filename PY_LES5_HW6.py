
subjects = {}

with open('text_HW6.txt', 'r') as les:
    for line in les.readlines():
        data = line.replace('(', ' ').split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
print(subjects)
