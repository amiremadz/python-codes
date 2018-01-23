#!/usr/bin/python
import copy

class MySort(object):
    def __init__(self, arr):
        self.arr = arr

    def bubble(self):
        result = copy.deepcopy(self.arr)
        
        idx1 = 0
        idx2 = len(result) - 1

        while(idx2 > 0):
            for idx1 in range(0, idx2):
                if result[idx1] > result[idx2]:
                    tmp = result[idx1]
                    result[idx1] = result[idx2]
                    result[idx2] = tmp
            idx2 -= 1    

        return result

    def selection(self):
        result = copy.deepcopy(self.arr)

        idx_end = len(result) - 1
        idx_sorted = 0

        while idx_sorted < idx_end:
            minval = result[idx_sorted]
            idx_minval = idx_sorted
            
            for idx in range(idx_sorted + 1, idx_end + 1):
                if result[idx] < minval:
                    minval = result[idx]
                    idx_minval = idx
            
            tmp = result[idx_sorted]
            result[idx_sorted] = result[idx_minval]
            result[idx_minval] = tmp

            idx_sorted += 1

        return result

if __name__ == "__main__":
    arr = [12, 4, 56, 23, 3, 67, 128, 44]
    srt = MySort(arr)
    
    print(srt.arr)
    
    bub = srt.bubble() 
    sel = srt.selection()
    
    print(bub)
    print(sel)

