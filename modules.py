import keyword
#
#
# def contains_keyword_v1(*args):
#     for k in args:
#         if keyword.iskeyword(k):
#             return True
#     return False


# def contains_keyword_v2(*args):
#     statuses = []
#     for k in args:
#         statuses.append(keyword.iskeyword(k))
#     if True in statuses:
#         return True
#     else:
#         return False


def contains_keyword_v3(*args):
    return any(keyword.iskeyword(k) for k in args)


print(contains_keyword_v3('banana', 'banana', 'True', 'banana'))