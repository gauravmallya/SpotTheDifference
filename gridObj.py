import numpy
class grids:
    def __init__(self, arr, size, rows):
        self.arr = arr
        self.size = size
        self.rows = rows
    
    def retValue(self, x, y):
        arrayVal = self.pos(x, y)
        return self.arr[arrayVal]
    def changeVal(self, x, y):
        arrayVal = self.pos(x, y)
        self.arr[arrayVal] = True

    def pos(self, x, y):
        distBtwRows = self.size // self.rows
        arrayVal = (y // distBtwRows) + (x// distBtwRows)  * self.rows
        return arrayVal

    def numInaccuracies(self):
        return len(self.arr) - numpy.count_nonzero(self.arr)
