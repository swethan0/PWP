# Program to read a text file line by line and store each line in a list

def read_file_to_list(filename):
    lines_list = []
    try:
        with open(filename, 'r') as file:
            # Read each line and strip newline character
            lines_list = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return lines_list


# Main program
filename = r"C:\Users\admin\Downloads\example.txt"   
lines = read_file_to_list(filename)

print("Contents of the file as a list:")
print(lines)

