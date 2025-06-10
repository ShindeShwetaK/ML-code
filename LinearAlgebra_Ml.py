def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float] | int:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    
    if len(a[0]) != len(b):  # Use a[0] not a[1] to avoid index error on small matrices
        return -1

    result = []
    
    for row in a:
        dot_product = 0
        for j in range(len(row)):
            dot_product += row[j] * b[j]
        result.append(dot_product)

    return result

#Transposr of a matrix
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    b = []

    for i in range(len(a[0])):
        new_row = []
        for j in a:
            new_row.append(j[i])
        b.append(new_row)

	return b
