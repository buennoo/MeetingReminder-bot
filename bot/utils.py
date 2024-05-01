from datetime import datetime

def check_hour(user_input):
    try:
        datetime.strptime(user_input, '%H:%M')
        return True
    except ValueError:
        return False
    
def check_date(user_input):
    try:
        datetime.strptime(user_input, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def return_date():
    return datetime.now()
