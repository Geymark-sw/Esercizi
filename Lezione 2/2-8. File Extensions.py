"""
2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename.
 Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
"""

file_name: str = "python_notes.txt"

print(file_name.removesuffix(".txt"))