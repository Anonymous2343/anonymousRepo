def process_metrics(file_path):
    col1_sum = col2_sum = col3_sum = col4_sum = 0
    total_rows = 0

    with open(file_path, 'r') as file:
        for line in file:
            col1, col2, col3, col4 = map(int, line.strip().split())
            col1_sum += col1
            col2_sum += col2
            col3_sum += col3
            col4_sum += col4
            total_rows += 1

    # Compute ratios
    col1_ratio = col1_sum / total_rows
    col2_ratio = col2_sum / total_rows
    col3_ratio = col3_sum / total_rows
    col4_ratio = col4_sum / total_rows

    # Output
    print("Summed Metrics:")
    print(f"Compilation Handwritten: {col1_sum}")
    print(f"Passes Handwritten:   {col2_sum}")
    print(f"Compilation Automatic:      {col3_sum}")
    print(f"Passes Automatic:        {col4_sum}\n")

    print("Ratios:")
    print(f"Compilation Rate Handwritten: {col1_ratio:.2f}")
    print(f"Passes Rate Handwritten:   {col2_ratio:.2f}")
    print(f"Compilation Rate Automatic:      {col3_ratio:.2f}")
    print(f"Passes Rate Automatic:        {col4_ratio:.2f}")

# Run the function with the specified file
process_metrics("comparison_output.txt")
