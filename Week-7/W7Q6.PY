def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def swap_lines(file1_path, file2_path):
    lines1 = read_file(file1_path)
    lines2 = read_file(file2_path)
    
    middle_index = len(lines1) // 2  # Integer division gives the middle index
    
    middle_line_content = lines1[middle_index].rstrip()  # Remove newline for clean output
    last_line_content = lines2[-1].rstrip()  # Last line of file 2
    
    lines1[middle_index] = last_line_content + '\n'
    lines2[-1] = middle_line_content + '\n'
    
    write_file(file1_path, lines1)
    write_file(file2_path, lines2)
    
    print(f'Swapped content:\nMiddle line in file 1: "{last_line_content}"\nLast line in file 2: "{middle_line_content}"')

def main():
    file1_path = 'file1.txt'
    file2_path = 'file2.txt'
    
    swap_lines(file1_path, file2_path)

if __name__ == "__main__":
    main()
