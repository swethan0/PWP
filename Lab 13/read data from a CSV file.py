import csv

# Program to read data from a CSV file and print each row
def read_csv_file(filename):
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            
            print("Contents of the CSV file:")
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Main program
filename = r"C:\Users\admin\Downloads\ABHI.csv"   
read_csv_file(filename)

