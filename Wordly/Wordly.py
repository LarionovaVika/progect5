from random import choice


print('Привет!/Hello!')
print('Это игра Wordly./This is a Wordly game.')
print('Правила игры:/The rules of the game:')
print('Игрок вводит слово той же длинны, что и исходное. Программа показывает буквы, которые находятся на своих местах и буквы, которые есть в слове, но положение их не угадано. Игрок вводит новое слово и т.д. Игра заканчивается когда угадано слово или введено 6 неправильных слов./The player enters a word of the same length as the original one. The program shows the letters that are in their places and the letters that are in the word, but their position is not guessed. The player enters a new word and so on. The game ends when a word is guessed or 6 incorrect words are entered.')
print('Удачи!/Good luck!')
print('Выберите язык(русский или английский)./Select a language(russian or english).')
a = input()
if a == 'русский' or a == 'russian':
    with open('russian.dict', encoding='utf-8') as f:
        words = f.read().rstrip().split()
        word = choice(words)
        print('Длина слова:', str(len(word)) + '.')
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
                    b += wordpl[i] + ' '
                    c += '_ '
                elif wordpl[i] in word:
                    c += wordpl[i] + ' '
                    b += '_ '
                else:
                    b += '_ '
                    c += '_ '
            print('Правильные буквы, находящиеся на своём метсе.')
            print(b)
            print('Буквы, который есть в этом слове, но находятся не на своём месте.')
            print(c)
        if d != 1:
            print('Правильное слово:', word)
else:
    with open('english.dict') as f:
        words = f.read().rstrip().split()
        word = choice(words)
        print('Word length:', str(len(word)) + '.')
        d = 0
        for u in range(6):
            wordpl = input()
            b = ''
            c = ''
            if word == wordpl:
                print('Well done! You guessed it.')
                d = 1
                break
            for i in range(len(word)):
                if word[i] == wordpl[i]:
                    b += wordpl[i] + ' '
                    c += '_ '
                elif wordpl[i] in word:
                    c += wordpl[i] + ' '
                    b += '_ '
                else:
                    b += '_ '
                    c += '_ '
            print('The correct letters are on their own metz.')
            print(b)
            print('The letters that are in this word, but are not in their place.')
            print(c)
        if d != 1:
            print('The right word:', word)
