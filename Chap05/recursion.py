def countdown(n):
    if n < 0:
        print('Blastoff')
    else:
        print(n)
        countdown(n-1)

def print_n_times(string, n):
    if n > 0:
        print(f'{string} - {n}')
        print_n_times(string, n-1)

print_n_times('Llama', 4)