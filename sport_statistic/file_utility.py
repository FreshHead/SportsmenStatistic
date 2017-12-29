import csv


def read(gio_file):
    with open(gio_file.get_path(), 'rt') as fin:
        cin = csv.reader(fin, delimiter='|')
        return [row for row in cin]
