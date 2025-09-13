def count_file_stats(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)

            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_chars}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")


# Run the program
count_file_stats(r"C:\Users\admin\Downloads\example.txt")


