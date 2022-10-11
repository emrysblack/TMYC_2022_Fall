import csv


def import_csv_flat(file_path):
    with open(file_path, mode ='r')as file:
        csvFile = csv.reader(file)
        # flatten lines to single list
        return [item for line in csvFile for item in line]

def main():
    print(import_csv_flat("test.csv"))

if __name__ == "__main__":
    main()