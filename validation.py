# validation.py - валидация данных для Bookin Service

from datetime import datetime, timedelta

def validate_dates(check_in, check_out):
    """Проверка дат бронирования"""
    try:
        check_in_date = datetime.fromisoformat(check_in)
        check_out_date = datetime.fromisoformat(check_out)
    except ValueError:
        return False, 'Неверный формат даты'
    
    if check_in_date < datetime.now():
        return False, 'Дата заезда не может быть в прошлом'
    
    if check_out_date <= check_in_date:
        return False, 'Дата выезда должна быть позже даты заезда'
    
    return True, 'OK'

def validate_price(price):
    """Проверка цены"""
    if price <= 0:
        return False, 'Цена должна быть больше 0'
    return True, 'OK'

def validate_phone(phone):
    """Проверка телефона"""
    import re
    pattern = r'^\+?[0-9]{10,15}$'
    if not re.match(pattern, phone):
        return False, 'Неверный формат телефона'
    return True, 'OK'

def validate_email(email):
    """Проверка email"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False, 'Неверный формат email'
    return True, 'OK'
