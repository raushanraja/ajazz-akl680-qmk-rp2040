import json


def replace_with_row_col(data):
    for row_idx, row in enumerate(data):
        col_count = 0  # Track the position for each string
        for col_idx, item in enumerate(row):
            if isinstance(item, str) and item:  # Replace only non-empty strings
                row[col_idx] = f"{row_idx},{col_count}"
                col_count += 1  # Increment only when a string is replaced
    return data


def format_dict(d):
    # Remove 'a' key if it exists and format the dictionary without quotes around keys
    if "a" in d:
        del d["a"]
    return "{" + ", ".join(f"{key}: {value}" for key, value in d.items()) + "}"


def format_row(row):
    formatted_row = []
    for item in row:
        if isinstance(item, str):
            formatted_row.append(f'"{item}"')
        elif isinstance(item, dict):
            formatted_row.append(format_dict(item))
    return "[" + ",".join(formatted_row) + "]"


def process_json_file(input_file, output_file):
    # Read the data from the JSON file
    with open(input_file, "r") as f:
        row_data = json.load(f)

    # Replace all strings with "row,column"
    updated_row_data = replace_with_row_col(row_data)

    # Format the updated data as JSON with square brackets and double quotes around strings
    formatted_data = [format_row(row) for row in updated_row_data]

    # Write the formatted data to the output file
    with open(output_file, "w") as f:
        f.write("[" + ",".join(formatted_data) + "]")


# Example usage
input_file = "input.json"  # Replace with your input JSON file path
output_file = "output.json"  # Replace with your desired output JSON file path

process_json_file(input_file, output_file)
