# Write a boolean function, is_between(x, y, z), that returns True if  x<y<z  or if  z<y<x , andFalse otherwise.

def is_between(x, y, z):
    teste1 = x < y < z
    teste2 = z < y < x
    
    return teste1 or teste2

print(is_between(1, 2, 3))
print(is_between(3, 2, 1))
print(is_between(1, 3, 2))
print(is_between(2, 3, 1))