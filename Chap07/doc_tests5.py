from doctest import run_docstring_examples

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def word_score(word, available):
    """Compute the score for an acceptable word.
    
    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """

    word = word.lower()
    available = available.lower()
    len_word = len(word)
    score = 0
    count_letter = 0

    # checa se todas letras da palavra estão em available
    for letter in word:
        if letter not in available:
            return score
       

    # checa se todas as letras de available estão na palavra
    for letter in available:
        if letter in word:
            count_letter += 1

    if count_letter == len(available):   # É um pangram
        score += len_word + 7

    elif len_word == 4: # tem quatro letras
        score = 1
        
    else:   # tem mais de 4 letras
        score = len_word

    return score