import csv


def read_flat(file_path):
    with open(file_path, mode ='r')as file:
        csvFile = csv.reader(file)
        # flatten lines to single list
        return [item for line in csvFile for item in line]

def main():
    print(read_flat("shared/test.csv"))

if __name__ == "__main__":
    main()