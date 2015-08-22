import string
import random

def generate_value(length=10):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(length))

def generate_uid(instance, length=10):
    uid = generate_value(length)
    while not instance.check_unique(uid):
        uid = generate_value(length)
    return uid
    
