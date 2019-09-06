from datetime import date
def convert_string_to_data(str):
    date_parts = [int(num_str) for num_str in str.split('/')]
    return date(date_parts[2], date_parts[1], date_parts[0])