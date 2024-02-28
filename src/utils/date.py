from datetime import datetime, timedelta


def convert_str_date_to_date(date: str, date_format: str = "%Y-%m-%dT%H:%M:%S"):
    if date is None or date == '':
        raise ValueError('Invalid date format')
    return datetime.strptime(date, date_format).date()


def convert_str_date_to_isoformat(date: str):
    return str(datetime.fromisoformat(date))


def get_date_from_now(type: str = None, days: int = 0):
    types = ['futures', 'past']
    if type not in types:
        return datetime.now().date()

    if type == 'futures':
        return datetime.now().date() + timedelta(days=days)
    elif type == 'past':
        return datetime.now().date() - timedelta(days=days)


def diff_date(start: str, end: str):
    end = convert_str_date_to_date(end, '%Y-%m-%d')
    start = convert_str_date_to_date(start, '%Y-%m-%d')
    return (end - start).days


def get_now_date():
    return str(datetime.now().date())
