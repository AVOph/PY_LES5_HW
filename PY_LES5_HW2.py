with open('text_HW2.txt', 'a+') as text_user:
    text_user.write(f'Привет\nкак дела\nу меня все хорошо\nа у тебя\n')
with open('text_HW2.txt', 'r') as text_user:
    # size=len([0 for _ in text_user])
    size = len([0 for _ in text_user])
with open('text_HW2.txt', 'r') as text_user:
    p = text_user.read()
    words = p.split()
    wordCount = len(words)
print(f'Количество слов: {wordCount}')
print(f'Количество строк: {size}')