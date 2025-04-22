import pandas as pd

def input_from_console():
    """
    Function:
        Reads text input from the console.

    Returns:
       text (str): User input from the console.
    """
    text = input("Enter your text: ")
    return text


def read_file_builtin():
    """
    Function:
        Reads data from a file using built-in Python functionality.

    Args:
        None

    Returns:
       content (str): Content of the file str
    """
    file_path = input("Enter the path to the file to read with built-in method: ")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"{file_path} in build-in reding results"
    except Exception as e:
        return f"Error reading file: {str(e)}"


def read_file_pandas():
    """
    Function:
        Reads data from a file using the pandas library.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        data: pandas DataFrame containing the file data.
    """
    file_path = input("Enter the path to the CSV file to read with pandas: ")
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        return f"{file_path} in pandas reding results"
    except Exception as e:
        return f"Error reading file with pandas: {str(e)}"
