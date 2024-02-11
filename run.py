import csv
import os
import glob
from datetime import datetime

# Function to convert date format
def convert_date_format(date_str):
    try:
        # Assuming the input format is mm/dd/yy and converting it to dd.mm.yyyy
        return datetime.strptime(date_str, '%m/%d/%y').strftime('%d.%m.%Y')
    except ValueError:
        # Return original string if conversion fails
        return date_str

# Define the output directory
output_directory = 'output'
# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Find the first CSV file in the current directory
csv_files = glob.glob('*.csv')
if csv_files:
    input_file_name = csv_files[0]  # Process the first CSV file found
    # Define the output file path
    output_file_name = 'your_data.csv'
    output_file_path = os.path.join(output_directory, 'your_data.csv')

    # Open the input file in read mode and output file in write mode
    with open(input_file_name, mode='r', encoding='utf-8') as infile, open(output_file_path, mode='w', encoding='utf-8', newline='') as outfile:
        # Create CSV reader and writer
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Iterate over each row in the input CSV
        for row in reader:
            # Check if the row is not empty
            if row:
                # Convert the date format for the third column (index 2)
                row[2] = convert_date_format(row[2])
            # Write the modified row to the output CSV
            writer.writerow(row)

    print(f"Conversion complete. Output saved to '{output_file_path}'.")
else:
    print("No CSV files found in the directory.")
