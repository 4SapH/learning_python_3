
x = 6


def example():
    print(x)
    print(x+5)

    # x+=6 ---> error (when modifying), x isn't global

example()


print()


def example_2():
    global x # x ---> global var (similar to a pointer?)
    print(x)
    x += 7
    print(x)

example_2()
print(x)


# global vars not recommeneded (usually)


print()


# hack:
def example_3():
    globx = x
    print(globx)
    globx+=19
    print(globx)
    # globx ---> local

    return globx

x = example_3()

print()

print(x)
