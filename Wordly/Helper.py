print('Привет! Это помощник для игры Wordly./Hi! This is an assistant for the Wordly game.')
print('Как работает помощник:/How the assistant works:')
print('По введенной маске и набору букв в слове выводит список подходящих слов./Based on the entered mask and the set of letters in the word, it displays a list of suitable words.')
print('Введите маску без пробелов(пример: __в___)./Enter a mask without spaces (example: __ in ___).')
b = input()
print('Выберете язык./Choose a language.')
a = input()
if a == 'русский' or a == 'russian':
    with open('russian.dict', encoding='utf-8') as f:
        words = f.read().rstrip().split()
        c = []
        for y in b:
            if y != '_':
                c.append(y)
        for i in words:
            if len(i) == len(b):
                d = 0
                for u in range(len(b)):
                    if b[u] == i[u]:
                        d += 1
                if d == len(c):
                    print('Возможные слова:')
                    print(i)
else:
    with open('english.dict') as f:
        words = f.read().rstrip().split()
        c = []
        for y in b:
            if y != '_':
                c.append(y)
        for i in words:
            if len(i) == len(b):
                d = 0
                for u in range(len(b)):
                    if b[u] == i[u]:
                        d += 1
                if d == len(c):
                    print('Possible words:')
                    print(i)
