"""HW7 file_stats.py
    Module file_stats that includes the stats function.
    $ python file_stats.py filename
    Prints out file statistics (see below).
    Calling stats(filename) returns 4 values:
    character_count - number of characters in the file.
    word_count - number of words in the file.
    line_count - number of lines in the file.
    longest_line - length of the longest line.
    See instructions for details.
"""
# Your name here 
import sys


def stats(filename):
    """Given a text file name, return file statistics in a tuple:
        number of characters in the file,
        number of words in the file (as defined by whitespace),
        number of lines in the file,
        number of characters of the longest line in the file.
    """
    # Do the calculations and return the tuple of data
    fn=open(filename)
    contents=fn.read()
    lines = len(contents.splitlines())
    characters = len(contents)
    words = len(contents.split())
    longest = max([len(i) for i in contents.splitlines()])

    return characters, words, lines, longest
    
    pass


if __name__ == '__main__':
    # call stats() with the filename given on the command line,
    # and print the results as shown in instructions.
    characters, words, lines, longest = stats(sys.argv[1])
    print(f"Characters: {characters}\nWords: {words}\nLines: {lines}\nLongest line: {longest}")
    
    pass
