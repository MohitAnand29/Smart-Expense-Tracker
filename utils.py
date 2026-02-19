import os
import datetime

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_date(date_text):
    """Validates date format YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_current_date():
    """Returns current date in YYYY-MM-DD format."""
    return datetime.date.today().strftime('%Y-%m-%d')

def get_current_month():
    """Returns current month in YYYY-MM format."""
    return datetime.date.today().strftime('%Y-%m')
