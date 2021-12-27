"""HW7 country_convert.py
    Read file 'countryInfo.csv' and create new file 'country_simple_info.csv'
    containing only country, capital and population; sorted by population.
    See instructions for details.
"""
# Your name here
import csv


def main():
    """Main program for country_convert.py"""
    infile = 'countryInfo.csv'
    outfile = 'country_simple_info.csv'
    with open(infile, 'r') as infile:

        csv_reader = csv.DictReader(infile, delimiter='\t')
        rows = list(csv_reader)

        def sort_key(rows):
            return int(rows['population'])

        rows.sort(key=sort_key)

    with open(outfile, 'w', newline='') as outfile:
        csv_writer = csv.DictWriter(outfile, fieldnames = ['name', 'capital', 'population'], extrasaction='ignore')
        csv_writer.writeheader()
        for i in rows:
            csv_writer.writerow(i)


    pass


if __name__ == "__main__":
    # There are no command line arguments for this program.
    main()
