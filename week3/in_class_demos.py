# Exercise 1: manually create a 2D data structure

#        elem    0  1  2      row
my_2dim_list = [[1, 2, 3],  # 0
                [4, 5, 6],  # 1
                [7, 8, 9]]  # 2
print(my_2dim_list[0][0])

# Exercise 2:
# sequential iteration over 2D
for row in my_2dim_list:
    for elem in row:
        print(elem, end=' ')
    print()

# Exercise 3:
# Dynamically build a 2D data structure and initialize with values
def make_2d(rows, cols, value=None):
    '''Create a rows x cols 2D data structure
    initialized to _value_
    Example:
    >>> made_2d(3, 3)
    [[None, None, None], [None, None, None], [None, None, None]]
    '''
    list_2d = []
    for _ in range(rows):
        elems = []
        for _ in range(cols):
            elems.append(value)
        list_2d.append(elems)
    return list_2d

# Exercise 3a:
# Refactor to list comprehension
def make_2d_cool(rows, cols, value=None):
    '''Same function as above implemented as a list comprehension
    '''
    return [[value for _ in range(cols)]
               for _ in range(rows)]

# Drive the code above...
print('#'*50)
print(make_2d_cool(3, 3, 42))
print('#'*50)
print(make_2d(3, 3, 42))


print('#'*50)

# Optional
# correct answer to initializing a list with sequential values
rows, cols = 3, 3
seq_2d = [[(j + 1) + (i*cols)
           for j in range(cols)]
           for i in range(rows)]

print(seq_2d)

