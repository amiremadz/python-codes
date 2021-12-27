"""Homework 6 for CSE-41273"""

# You need to import something from itertools:
from itertools import cycle


# 1. separate
# Create your own arguments to match the instructions.
def separate(string, sort=False):
    """Return a list of all characters in given string.
        If keyword argument sort is True, then return them sorted."""
    x=[]
    for i in string:
         x.append(i.lower())
    if sort == True:
        return sorted(x)
    else:
        return x



# 2. number_of_vowels
def number_of_vowels(string):
    """Returns the number of vowels in the input string."""
    count=0
    for i in string:
        if i.lower() in ('a', 'e', 'i', 'o', 'u'):
            count=count+1
    return count



# 3. special_nums
def special_nums():
    """Return a generator that yields, in order, the numbers that:
        Are in the range from 1 to 300 and are evenly divisible by 10 and 6."""

    for x in range(1,301):
        if x%10==0 and x%6==0:
            yield x


# 4. evens
def evens(sequence):
    """Return a generator that returns all the input numbers that are even."""

    for i in sequence:
        if i%2 ==0:
            yield i


# 5. continuous1234
def continuous1234():
    """Return a generator that returns the numbers 1, 2, 3, 4 continuously."""
    from itertools import cycle
    return cycle([1,2,3,4])


# 6. reverse_iter
def reverse_iter(iterable):
    """Return a generator that yields items from iterable in reverse order"""
    list=iterable[ : :-1]
    for i in list:
        yield i

# 7. ReverseIter class
class ReverseIter:
    """Class whose instances iterate the initial iterable in reverse order"""
    def __init__(self, list ):
        self.number = len(list)
        self.list =list

    def __iter__(self):
        return self

    def __next__(self):
        self.number -=1

        if self.number < 0:
            raise StopIteration()

        return self.list[self.number]
