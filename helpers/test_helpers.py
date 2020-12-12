import random
import string


def get_random_string(size=7):
    return ''.join(random.choices([*string.ascii_letters, *string.digits], k=size))
