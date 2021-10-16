from random import *

list_ = ['up','down','left','right']
random_list = [choice(list_) for i in range(20)]
def step(list):
    str_ = ''.join(list)
    if str_.count('left') == str_.count('right') and str_.count('up') == str_.count('down'):
        print(str_.count('right'), str_.count('left'), str_.count('up'). str_.count('down'))
        return True
    print(str_.count('right'), str_.count('left'), str_.count('up'), str_.count('down'))
    return False
print(step(random_list))