from random import choice, randint, randrange


def get_random_color():
    """得到一个随机色"""
    r = randint(0, 255);
    g = randint(0, 255);
    b = randint(0, 255);
    return (r, g, b);
