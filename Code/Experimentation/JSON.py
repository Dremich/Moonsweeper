import json

# Python object (dictionary)
data = {
    "row": 1,
    "col": 2,
    "flag": True,
}

# Create a 2D array
# Define the dimensions of the 2D array
rows = 3
cols = 4

# Create a 2D array
two_d_array = []

# Fill the 2D array with values using a nested for loop
for i in range(rows):
    row = []
    for j in range(cols):
        # Example: Fill each cell with its row * column index
        value = i * cols + j
        row.append(value)
    two_d_array.append(row)

# # Print the 2D array
# for row in two_d_array:
#     print(row)


# Serialize to JSON string
json_string = json.dumps(data)

print(json_string)  # Output: {"name": "John", "age": 30, "city": "New York"}

data2 = json.loads(json_string)