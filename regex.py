import re


def is_valid_time(t):
    time_regex = re.compile(r'^\d{1,2}:\d{2}$')
    match = time_regex.search(t)
    if match:
        return True
    return False


is_valid_time("11:55")