def has_e(word):
    for letter in word:
        if letter == 'E' or letter == 'e':
            return True
        else:
            return False

print(has_e('Gadsby'))
print(has_e('Emma'))