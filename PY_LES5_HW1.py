def input_text():
    text = f'{input("Введите текст для остановки введите пробел: ")}'
    if text != ' ':
        text_user.write(f'{text}\n')
        input_text()
    else:
        return

with open('text_HW1.txt', 'w') as text_user:
    input_text()

