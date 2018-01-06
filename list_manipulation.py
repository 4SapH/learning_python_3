'''

list
list[index]

list.append(value)
    .insert(index, value)
    .remove(value) ---> removes first found value
    .remove(list[index])
    .index(element) ---> finds first index of element
    .count(element) ---> counts occurences of element
    .sort()

# slice
list[index]
    [start:] ---> prints all from start
    [start:end] ---> inclusive start, exclusive end

list[-index] ---> starts from the end
                  ex. list[-1] = last element

'''
x = [5, 6, 2, 1, 6, 7, 2, 2, 6, 7, 2]

x.sort()
print(x)
