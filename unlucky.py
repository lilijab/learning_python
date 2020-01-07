for n in range(1,21):
    if n == 4 or n==13:
        state = 'UNLUCKY!'
    elif n % 2 == 0:
        state = 'Even'
    else:
        state = 'Odd'
    print(f'{n}: {state}')