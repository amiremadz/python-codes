"""HW7 re_sort.py
    Module re_sort that includes re_sort function.
    $ python re_sort.py in_file.csv
    Sorts in_file by second of the CSV columns into "in_file_sort.csv"
    Or calling re_sort(in_file, out_file)
    Sorts in_file by second of the CSV columns into out_file.
    See instructions for details.
"""
# Your name here
import csv
import sys
import pathlib


def re_sort(in_file, out_file):
    """Re-sort the given CSV file by the second column."""
    with open(in_file) as infile:
        with open(out_file, mode='w', newline='') as outfile:
            csv_reader = csv.reader(infile)
            csv_writer = csv.writer(outfile)
            head_row = next(csv_reader)
            remaining_rows=list(csv_reader)

            def sort_key(column):
                return column[1]
            sorted_array=sorted(remaining_rows, key=sort_key)
            csv_writer.writerow(head_row)
            for i in sorted_array:
                csv_writer.writerow(i)



    pass


if __name__ == "__main__":
    p=pathlib.Path(sys.argv[1])
    fname=p.stem + '_sorted' + p.suffix
    newpath =p.parent/fname
    re_sort(sys.argv[1], newpath)
    pass
