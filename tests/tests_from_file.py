from unittest.mock import patch, mock_open

import pandas as pd

from app.io.input import read_file_builtin, read_file_pandas


def test_read_file_builtin_successful():
    mock_file_content = "This is test content"
    with patch('builtins.input', return_value="test_file.txt"), \
         patch('builtins.open', mock_open(read_data=mock_file_content)):
        result = read_file_builtin()
        assert result == mock_file_content

def test_read_file_builtin_file_not_found():
    with patch('builtins.input', return_value="nonexistent_file.txt"), \
         patch('builtins.open', side_effect=FileNotFoundError):
        result = read_file_builtin()
        assert result == "nonexistent_file.txt in build-in reding results"

def test_read_file_builtin_general_exception():
    with patch('builtins.input', return_value="test_file.txt"), \
         patch('builtins.open', side_effect=Exception("Test error")):
        result = read_file_builtin()
        assert result == "Error reading file: Test error"

def test_read_file_pandas_successful():
    mock_df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    with patch('builtins.input', return_value="test_file.csv"), \
         patch('pandas.read_csv', return_value=mock_df):
        result = read_file_pandas()
        assert isinstance(result, pd.DataFrame)
        assert result.equals(mock_df)

def test_read_file_pandas_file_not_found():
    with patch('builtins.input', return_value="nonexistent_file.csv"), \
         patch('pandas.read_csv', side_effect=FileNotFoundError):
        result = read_file_pandas()
        assert result == "nonexistent_file.csv in pandas reding results"

def test_read_file_pandas_general_exception():
    with patch('builtins.input', return_value="test_file.csv"), \
         patch('pandas.read_csv', side_effect=Exception("Test pandas error")):
        result = read_file_pandas()
        assert result == "Error reading file with pandas: Test pandas error"