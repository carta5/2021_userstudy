import random
import string

def get_random_string(length=20):
    candidate_char = string.ascii_letters + string.digits
    return ''.join(random.choices(candidate_char, k=length))
