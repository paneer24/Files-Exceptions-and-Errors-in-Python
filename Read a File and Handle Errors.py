def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"Error: {e}")
filename = 'sample.txt'
read_file(filename)
