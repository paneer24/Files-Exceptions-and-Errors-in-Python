Task 1 Read a File and Handle Errors 
1) The read_file function takes a filename parameter and attempts to open the file in read mode ('r').
2) It iterates through each line in the file using a for loop and prints each line using print(line.strip()). The strip() method removes any extra newline characters for cleaner output.
3) It uses exception handling to catch specific errors:
   - FileNotFoundError is caught if the specified file does not exist.
   - Exception catches any other unexpected errors that might occur during file handling.
   
Task 2 Write and Append data to a file
1) write_to_file(filename):
   -Takes user input.
   - Writes it to output.txt, overwriting any existing content.
2) append_to_file(filename):
   - Takes additional user input.
   - Appends it to output.txt.
3) read_file(filename):
   - Reads and prints the final content of the file.
   - Handles cases where the file does not exist.
