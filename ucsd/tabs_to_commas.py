"""HW7 tabs_to_commas.py
    Module tabs_to_commas that includes function tab_to_comma
    $ python tabs_to_commas in_file.tsv
    Creates new file in_file_commas.csv with tabs delimiters changed
    to commas. In_file can be csv named.
    See instructions for details.
"""
# Your name here
import csv
import sys


def tab_to_comma(in_file, out_file):
    """Read tab-delimited file and write CSV file back out."""
    with open(in_file) as infile:
        with open(out_file, 'w', newline='') as outfile:
          csv_reader = csv.reader(infile, delimiter = '\t')
          csv_writer = csv.writer(outfile, delimiter = ',')
          for i in csv_reader:
                csv_writer.writerow(i)

    pass


if __name__ == "__main__":
    tab_to_comma(sys.argv[1], sys.argv[2])
    pass
