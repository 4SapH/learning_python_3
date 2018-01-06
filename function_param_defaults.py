

# normal definition
def simple(num1, num2):
    pass


#default parameter
def simple(num1, num2=5):
    print(num1, num2)

simple(2)



#example
def basic_window(width, height, font='TNR',
                bgc='w', scroll_bar=True):
    print(width, height, font, bgc)

basic_window(500, 350)
basic_window(500, 300, 'a')
basic_window(500, 300, bgc='b') # more common,
                                # font is uneffected
