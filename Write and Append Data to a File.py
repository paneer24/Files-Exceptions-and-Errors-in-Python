def write_to_file(filename):
    data = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(data + '\n')

def append_to_file(filename):
    data = input("Enter text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(data + '\n')

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("\nFinal content of the file:")
            print(file.read())
    except FileNotFoundError:
        print("Error: The file does not exist.")

filename = 'output.txt'

write_to_file(filename)
append_to_file(filename)
read_file(filename)
