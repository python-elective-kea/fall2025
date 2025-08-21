# counter_module.py

count = 0

def increment():
    global count
    count += 1
    return count

def get_count():
    return count
