#!//usr/bin/env python3

'''
 Writing a basci sudoku check
'''

def isuniq(_list):
    '''
    _list: provide a list of elemets and check if all the elemets are uniq
    return: bool
    '''
    _set = set()
    for element in _list:
        if element in _set: return False
        _set.add(element)
    return True
    

test_puzzle = [
[1,2,3,4,5,6,7,8,9],
[4,5,6,7,8,9,1,2,3],
[7,8,9,1,2,3,4,5,6],
[2,7,1,3,6,4,8,9,5],
[8,3,5,2,9,1,6,4,7],
[9,6,4,5,7,8,2,3,1],
[3,1,2,6,4,5,9,7,8],
[5,9,7,8,1,2,3,6,4],
[6,4,8,9,3,7,5,1,2],
]

for row in test_puzzle:
    print(f"The row :{row} is {'Valid' if isuniq(row) else 'InValid'}")




