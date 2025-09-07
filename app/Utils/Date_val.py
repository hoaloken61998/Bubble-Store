from datetime import  datetime
from PyQt6.QtWidgets import QMessageBox

def check_input(date_first, date_last):
    date_format = "%m/%d/%Y"  # Define the expected date format

    if not is_valid_date(date_first, date_format):
        QMessageBox.warning(None, 'Invalid Date', 'The "From" date is not a valid date.')
        return False

    if not is_valid_date(date_last, date_format):
        QMessageBox.warning(None, 'Invalid Date', 'The "To" date is not a valid date.')
        return False

    # If both dates are valid
    return True

def is_valid_date(date_str, date_format):
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False