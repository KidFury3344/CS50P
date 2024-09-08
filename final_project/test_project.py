import pytest
from unittest.mock import patch, mock_open
from project import file_read, select_file_graphically, terminal_view, get_file, get_view

@pytest.fixture
def mock_csv_data():
    return 'question,answer\nQ1,A1\nQ2,A2\n'

def test_get_view(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert get_view() == "commandline"

def test_file_read_success(mock_csv_data):
    with patch('builtins.open', mock_open(read_data=mock_csv_data)):
        flashcards = file_read('dummy_path.csv')
        assert flashcards == [['question', 'answer'], ['Q1', 'A1'], ['Q2', 'A2']]



def test_get_file_command_line(monkeypatch):
    monkeypatch.setattr('sys.argv', ['script_name.py', 'dummy_path.csv'])
    monkeypatch.setattr('os.path.exists', lambda path: True)
    assert get_file() == 'dummy_path.csv'

def test_get_file_input(monkeypatch):
    monkeypatch.setattr('sys.argv', ['script_name.py'])
    monkeypatch.setattr('builtins.input', lambda _: 'dummy_path.csv')
    monkeypatch.setattr('os.path.exists', lambda path: True)
    assert get_file() == 'dummy_path.csv'

