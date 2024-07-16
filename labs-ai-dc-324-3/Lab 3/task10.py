def generate_2d_array(m, n):
    # Initialize an empty list to store the 2D array
    array = []
    
    # Loop over each row index from 0 to m-1
    for i in range(m):
        # Initialize an empty list for the current row
        row = []
        
        # Loop over each column index from 0 to n-1
        for j in range(n):
            # Calculate the element value as i * j and append it to the current row
            row.append(i * j)
    
        # Append the completed row to the array
        array.append(row)
    
    return array

# Input for number of rows and columns
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

# Generate the 2D array
result = generate_2d_array(m, n)

# Print the generated 2D array
print("Generated 2D array:")
for row in result:
    print(row)