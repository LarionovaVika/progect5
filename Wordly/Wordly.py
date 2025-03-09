from random import choice


a = input()
if a == 'русский':
    with open('russian.dict', encoding='utf-8') as f:
        words = f.read().rstrip().split()
        word = choice(words)
        print('Длина слова:', str(len(word)))
        d = 0
        for u in range(6):
            wordpl = input()
            b = ''
            c = ''
            if word == wordpl:
                print('Молодец! Ты угадал.')
                d = 1
                break
            for i in range(len(word)):
                if word[i] == wordpl[i]:
                    b += wordpl[i]
                    c += '_'
                elif wordpl[i] in word:
                    c += wordpl[i]
                    b += '_'
                else:
                    b += '_'
                    c += '_'
            print(b)
            print(c)
        if d != 1:
            print('Правильное слово:', word)
