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

    def insertion(self):
        result = copy.deepcopy(self.arr)

        for idx in range(1,len(result)):
            pos = idx
            value = result[idx]

            while (pos > 0) and (result[pos - 1] > value):
                result[pos] = result[pos - 1]
                pos -= 1
            
            result[pos] = value

        return result

    def insertion_gap(self, arr, gap):
        start = 0
        for idx in range(start + gap, len(arr), gap):
            pos = idx
            value = arr[idx]

            while (pos > 0) and (arr[pos - gap] > value):
                arr[pos] = arr[pos - gap]
                pos -= gap

            arr[pos] = value

    def shell(self):
        result = copy.deepcopy(self.arr)
        gap = int(len(result) / 2)

        while gap > 0:
            self.insertion_gap(result, gap)
            gap = int(gap / 2)
            
        return result

    def merge_helper(self, arr):

        length = len(arr)

        if length == 1:
            return
        mid = int(length/2)    
        left  = arr[:mid]
        right = arr[mid:]

        self.merge_helper(left)
        self.merge_helper(right)

        idx_l = 0
        idx_r = 0
        idx = 0

        while idx_l < len(left) and idx_r < len(right):
            if left[idx_l] <= right[idx_r]:
                arr[idx] = left[idx_l]
                idx_l += 1
            else:
                arr[idx] = right[idx_r]
                idx_r += 1
            idx += 1

        if idx_l < len(left):
            arr[idx:] = left[idx_l:]
        if idx_r < len(right):
            arr[idx:] = right[idx_r:]

    def merge(self):
        result = copy.deepcopy(self.arr)
        
        self.merge_helper(result)
        
        return result

    def quick(self):
        result = copy.deepcopy(self.arr)
        return self.quick_helper(result, 0, len(result) - 1)

    def quick_helper(self, arr, lo, hi):
        if(lo >= hi):
            return 
        
        splitpoint = self.__partition(arr, lo, hi)
        self.quick_helper(arr, lo, splitpoint - 1)
        self.quick_helper(arr, splitpoint + 1, hi)

    def __partition(self, arr, lo, hi):
        pivot = arr[lo]
        leftmark  = lo + 1
        rightmark = hi

        done = False

        while not done:
            while (leftmark <= rightmark) and (arr[leftmark] <= pivot):
                leftmark += 1
            
            while (rightmark >= leftmark) and (arr[rightmark] >= pivot):
                rightmark -= 1
            
            if (rightmark < leftmark):
                done = True
            else:
                tmp = arr[leftmark]
                arr[leftmark] = tmp
                arr[rightmark] = tmp

        tmp = arr[lo]
        arr[lo] = arr[rightmark]
        arr[rightmark] = tmp

        return rightmark


if __name__ == "__main__":
    arr = [12, 4, 56, 23, 56,  3, 67, 128, 44]
    srt = MySort(arr)
    
    print(srt.arr)
    
    bub = srt.bubble() 
    sel = srt.selection()
    ins = srt.insertion()
    shl = srt.shell()
    mrg = srt.merge()
    qck = srt.quick()

    print(bub)
    print(sel)
    print(ins)
    print(shl)
    print(mrg)
    print(qck)
