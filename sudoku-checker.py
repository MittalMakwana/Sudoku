#!//usr/bin/env python3

'''
 Writing a basci sudoku check
'''

class Sudoku(object):

    def __init__(self,puzzle):
        _puzzle = {}
        for number, row in enumerate(range(9)):
            _puzzle[row] = puzzle[number]
        self.puzzle = _puzzle



    def __str__(self):
        return "Sudoku puzzle"

    def display(self):
        for row_num, row in self.puzzle.items():
            if row_num in [0,3,6] : print("---+---+---")
            print(f"{i for i in row }")


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
    
def coloum(puzzle, coloum_num):
    return [row[coloum_num] for row in puzzle]

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


for _ in range(9):
    print(f"The coloum : { coloum(test_puzzle, _) } is { 'Valid' if isuniq(coloum(test_puzzle, _)) else 'Invalid' }")

_list=[]

for i in test_puzzle:
    print(i)

for i in range(4,7):
    for j in range(4,7):
        _list.append(test_puzzle[j][i])
a = Sudoku(test_puzzle)
a.display()
print(a)
