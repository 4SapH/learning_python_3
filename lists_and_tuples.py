'''

tuples ---> generate faster
       ---> are iterated faster
       ---> are immutable

       ---> usually used for collections of heterogeneous object

       ---> used for sequence unpacking (?)

var[index]
'''


# tuples
x = 5, 6, 2, 6
y = (5, 6, 2, 6)

# lists
y = [5, 6, 2, 6]


def example_func():
    return 15, 6

x, y = example_func()
print(x, y)
