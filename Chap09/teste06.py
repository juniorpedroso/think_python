def anagrama(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)

print(anagrama('amor', 'roda'))
