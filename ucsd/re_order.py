"""HW7 re_order.py
    Module re_order that includes the re_order function.
    $ python re_order.py in_file, out_file
    Or calling re_order.py(in_file, out_file)
    Where in_file is a CSV file with at least 2 columns.
    This will result in out_file having the same data as in_file,
    but with columns 1 and 2 reversed.
    See instructions for details.
"""
# Your name here
import csv
import sys


def re_order(in_file, out_file):
    """Read CSV file, swap first two columns, and output new file."""
    with open(in_file, 'r') as infile:
        with open(out_file, 'w', newline='') as outfile:
            csv_reader=csv.reader(infile)
            csv_writer=csv.writer(outfile)
            for i in csv_reader:
                x=i[0]
                i[0]=i[1]
                i[1]=x
                csv_writer.writerow(i)
    pass


if __name__ == "__main__":
    re_order(sys.argv[1], sys.argv[2])
    pass


