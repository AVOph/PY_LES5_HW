
nums = "12 7.2 87 93.5 0 32 7.1"
summ = 0

with open('text_HW5.txt', 'w') as textnums:
        textnums.write(nums)
with open('text_HW5.txt', 'r') as numssplit:
        data = numssplit.read()
for item in data.split():
    summ += float(item)
print(summ)
