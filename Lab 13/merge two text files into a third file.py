# Program to merge two text files into a third file

def merge_files(file1, file2, merged_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(merged_file, 'w') as mf:
            # Write contents of file1 first
            mf.write(f1.read())
            mf.write("\n")  # Add a newline between contents (optional)
            # Write contents of file2
            mf.write(f2.read())
        print(f"Files '{file1}' and '{file2}' have been merged into '{merged_file}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

# Main program
file1 = r"C:\Users\admin\Downloads\example.txt"
file2 = r"C:\Users\admin\Downloads\example2.txt"
merged_file = "merged.txt"

merge_files(file1, file2, merged_file)
