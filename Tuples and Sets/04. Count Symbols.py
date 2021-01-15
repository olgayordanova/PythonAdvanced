text = list(input())
letters_set = sorted(list(set(text)))
for letter in letters_set:
    print(f'{letter}: {text.count(letter)} time/s')

