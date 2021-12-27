#prin""" CLI program to for HW3 homework """
# Put your name here

import math
import argparse
from HW3 import words_containing, len_safe, unique

if __name__ == "__main__":
    # Set up argparse parser and arguments here
    parser = argparse.ArgumentParser(epilog='Does print, combine, then len. If no flags given, does nothing.')
    # Add the arguments here
    parser.add_argument('texts', help='Input strings to operate on', nargs='+')
    parser.add_argument('-p', '--print', help='Just print the input strings', action='store_true')
    parser.add_argument('-c', '--combine', help='Print input strings combined in a continuous string', action='store_true')
    parser.add_argument('-l', '--len', help='Print the lengths of the input strings', action='store_true')
 
    args = parser.parse_args()
    #print(args)

    # execute whatever the flags say to do here
    if args.print:
        print(' '.join(args.texts))

    if args.combine:
        print(''.join(args.texts))

    if args.len:
        for txt in args.texts:
            print(len(txt), end='')
            print(' ', end='')
        print('\n', end='')

    # If you prefer to call a single main() function written above the
    # if __name__ == "__main__":
    # statement, that is OK with me.
    # The important thing is to make it work correctly. ;-)
    # But don't overthink things.

    ### Part1: words_containing

    sentence = "Anyone who has never made a mistake has never tried anything new"

    result = words_containing(sentence, 'a')
    result.sort()
    gt = ['Anyone', 'has', 'made', 'a', 'mistake', 'has', 'anything']
    gt.sort()
    assert(result == gt)

    result = words_containing(sentence, 'x')
    result.sort()
    gt = []
    assert(result == gt)

    result = words_containing('', 'x')
    result.sort()
    gt = []
    assert(result == gt)

    sentence = 'The cow jumped over the moon'
   
    result = words_containing(sentence, 't')
    result.sort()
    gt = ['The', 'the']
    gt.sort()
    assert(result ==gt)

    result = words_containing(sentence, 'o')
    result.sort()
    gt = ['cow', 'over', 'moon']
    gt.sort()
    assert(result == gt)

    ### Part2: len_safe
    my_dict = {'a': 23, 'b': 8}
    assert(len_safe(my_dict) == 2)
    
    assert(len_safe([]) == 0)

    assert(len_safe(0.25) == -1)

    assert(len_safe(7) == -1)

    assert(len_safe(None) == -1)

    assert(len_safe('cat') == 3)

    assert(len_safe('') == 0)

    animals = ['dog', 'cat', 'bird', 'cat', 'fish']
    assert(len_safe(animals) == 5)

    assert(len_safe(math.pi) == -1)

    ### Part 3: unique
    numbers = [4, 5, 2, 6, 2, 3, 5, 8]
    nums = unique(numbers)
    assert(next(nums) == 4)
    assert(next(nums) == 5)
    assert(next(nums) == 2)
    assert(next(nums) == 6)
    assert(next(nums) == 3)
    assert(next(nums) == 8)
    try:
        next(nums)
    except:
        pass
        #print('StopIteation')

    things = unique(['dog', 'cat', 'bird', 'cat', 'fish'])
    assert(next(things) == 'dog')
    assert(next(things) == 'cat')
    assert(next(things) == 'bird')
    assert(next(things) == 'fish')
    try:
        next(things)
    except:
        pass
        #print('StopIteation')
