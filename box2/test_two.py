from .convert import convert_string_to_data
from datetime import date

def test_convert_data():
    assert convert_string_to_data('10/02/2019') == date(2019, 2, 10)

