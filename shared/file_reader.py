import csv


def read_csv_flat(file_path):
    with open(file_path, mode ='r')as file:
        csvFile = csv.reader(file)
        # flatten lines to single list
        return [item for line in csvFile for item in line]

def read_chars_multiple_lines(file_path):
    with open(file_path, mode ='r')as file:
        return [[item for item in line if not item.isspace()] for line in file.readlines()]

def main():
    print(read_csv_flat("shared/test.csv"))
    print(read_chars_multiple_lines("shared/test_multiple.txt"))

if __name__ == "__main__":
    main()