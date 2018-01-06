'''
[] = optional (in this examples, not actual syntax)


# usage: module_name.member_name

import module_name [as short_hand]


# for these you don't have to use module_name.member_name (just member_name)

from module_name import var_or_property [as short_hand]
from module_name import var_1 [as short_1], var_2 [as short_2], etc.

from module_name import * ---> all

'''

import statistics as s
example_list = [4, 6, 2, 5]
x = s.variance(example_list)
print(x)


from statistics import variance
print (variance(example_list))


from statistics import variance as v
print (v(example_list))


from statistics import variance, mean
x = variance(example_list)
y = mean(example_list)
print(x)
print(y)


from statistics import variance as v, mean as m
print(v(example_list))
print(m(example_list))


# to import everything
from statistics import *
print(variance(example_list))
print(median(example_list))
print(stdev(example_list))
print(mean(example_list))
