
import csv


# data = [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}]
def write_list_of_dicts_to_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def main(filename):
    data = read_csv_to_dict(filename)
    for row in data:
        print(row)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('sample_grocery.csv')
