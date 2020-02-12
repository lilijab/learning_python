def calculate(**kwargs):
    operation = kwargs.get('operation')
    first = kwargs.get('first', 0)
    second = kwargs.get('second', 0)
    make_float = kwargs.get('make_float', False)
    message = kwargs.get('message', 'The result is')

    if operation == 'add':
        result = first + second
    elif operation == 'subtract':
        result = first - second
    elif operation == 'multiply':
        result = first * second
    else:
        result = first / second

    if make_float:
        return '{} {}'.format(message, float(result))
    else:
        return '{} {}'.format(message, int(result))


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
