def output_to_console(text):
    """
    Function to output text to console.
    Args:
        text: The text to be displayed on the console
    """
    print(text)

def write_to_file_builtin(text, file_path=None):
    """
Function:
  write text to a file using built-in Python capabilities
Args:
  text: The text to be written to the file
  file_path: Path to the output file (optional)
Returns:
  str: Message indicating success or failure
    """

    if file_path is None:
        file_path = input("Enter the path for the output file: ")

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(text))
        return f"Data successfully written to {file_path}"
    except Exception as e:
        return f"Error writing to file: {str(e)}"

