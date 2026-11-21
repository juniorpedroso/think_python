from doctest import run_docstring_examples

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.
    
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('Python', 'nry')
    False
    >>> uses_none('Llama', 'cju')
    True
    """

    for letter in word.lower():
        if letter in forbidden.lower():
            return False

    return True

#run_doctests(uses_none)

def uses_only(word, available):
    """Checks whether a word uses only the available letters.
    
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('Antonio', 'antoi')
    True
    >>> uses_only('Aaaaa', 'a')
    True
    """

    for letter in word.lower():
        if letter not in available.lower():
            return False

    return True

run_doctests(uses_only)
