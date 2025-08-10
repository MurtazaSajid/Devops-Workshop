# Outer loop for numbers 1 to 10
for i in range(1, 11):
    # Inner loop for multiplying with 1 to 10
    for j in range(1, 11):
        print(f"{i} × {j} = {i*j}", end="\t")  # Tab spacing
    print()  # Newline after each row
