from app.io.input import *
from app.io.output import *

def main():

    print("\nConsole Input")
    console_text = input_from_console()

    print("\nFile Reading (Built-in)")
    builtin_text = read_file_builtin()

    print("\nFile Reading (Pandas)")
    pandas_data = read_file_pandas()

    print("\nResults Output")
    print("\nResults from console input: ")
    output_to_console(console_text)

    print("\nResults from built-in file reading:")
    output_to_console(builtin_text)

    print("\nResults from pandas file reading:")
    output_to_console(pandas_data)

    print("\nWriting Results to Files")
    write_to_file_builtin(console_text, "console_input_results.txt")
    write_to_file_builtin(builtin_text, "builtin_reading_results.txt")
    write_to_file_builtin(str(pandas_data), "pandas_reading_results.txt")

    print("\nAll results have been processed.")


if __name__ == "__main__":
    main()
