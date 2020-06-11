from csv import reader


def find_user(first_name, last_name):
    with open("users.csv") as file:
        document = list(reader(file))
        for element in document:
            if [first_name, last_name] == element:
                return document.index(element)
        return "{} {} wasn't found.".format(first_name, last_name)


print(find_user('Grace', 'Hopper'))