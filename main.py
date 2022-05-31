import csv

animal = input("What kind of animal are you interested in? ")
file_name = animal + '.csv'
# check if requested file exists
file_path = (f'./data/{file_name}')
try:
    file = open(file_path)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        print(f'{row[0]} is a {row[1]} year old {row[2]}')
    file.close()
except:
    print(f"Sorry, we don't have any {animal} here")
    exit()

# with open(file_path) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')