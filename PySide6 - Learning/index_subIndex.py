import csv

zeroth_column_values = []

with open('../Pyside6 - QStack/v3.0.0 - Akash_m2 (1) (2).csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Iterate over each row in the CSV file
    for row in csv_reader:
        zeroth_column_values.append(row[0])

# Print the list of values from the first column
# print(first_column_values)
zeroth_column_values = zeroth_column_values[1:]
print(zeroth_column_values)

int_addresses = [int(hex_address, 16) >> 8 for hex_address in zeroth_column_values]
print(int_addresses)
print("\n")

# Initialize an empty dictionary to store counts
number_counts = {}

# Count occurrences of each number
for num in int_addresses:
    if num in number_counts:
        number_counts[num] += 1
    else:
        number_counts[num] = 1


# Initialize separate variables to store counts
count_0 = number_counts.get(0, 0)
count_1 = number_counts.get(1, 0)
count_2 = number_counts.get(2, 0)
count_3 = number_counts.get(3, 0)
count_4 = number_counts.get(4, 0)
count_5 = number_counts.get(5, 0)
count_6 = number_counts.get(6, 0)
count_7 = number_counts.get(7, 0)
count_8 = number_counts.get(8, 0)
count_9 = number_counts.get(9, 0)
count_10 = number_counts.get(10, 0)

count_list = []
for i in range(11):
    count = locals().get(f"count_{i}", None)
    if count is not None:
        count_list.append(count)
        print(f"Count of {i}: {count}")


print(count_list)