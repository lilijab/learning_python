def extract_full_name(l):
    return [' '.join(l[0].values()), ' '.join(l[1].values())]

    # Provided solution:
    # return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))


print(extract_full_name([{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]))