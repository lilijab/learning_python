def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('Please do not divide by zero')
    except TypeError:
        print('Please provide two integers or floats')