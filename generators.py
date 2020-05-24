def make_song(count=99, beverage='soda'):
    for num in range(count, -1, -1):
        if num > 1:
            yield '{} bottles of {} on the wall.'.format(num, beverage)
        elif num == 1:
            yield 'Only {} bottle of {} left!'.format(num, beverage)
        else:
            yield 'No more {}!'.format(beverage)


def get_multiples(num=1, count=10):
    for n in range(1, count+1):
        yield num*n


def get_unlimited_multiples(num=1):
    multiplier = 1
    while True:
        new_num = num*multiplier
        yield new_num
        multiplier += 1